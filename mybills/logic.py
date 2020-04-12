import calendar
from datetime import datetime
from django.db.models import Q
from mybills.models import Expense, Income, Transfer


def sort_balance_items_by_date(balance_items):
    """ Sort list items by date and operation type"""
    balance_items.sort(key=lambda balance_item: (balance_item['date'], balance_item['operation_id']))


def range_date_from_beginning(year, month=None):
    # begin period
    begin_date = datetime(1970, 1, 1)
    # end period
    end_month = 12 if month is None else month
    end_date = datetime(year=year,
                        month=end_month,
                        day=calendar.monthrange(year, end_month)[1])
    return tuple([begin_date, end_date])


def range_date_specific(year, month=None):
    # begin period
    begin_month = 1 if month is None else month
    begin_date = datetime(year=year, month=begin_month, day=1)
    # end period
    end_month = 12 if month is None else month
    end_date = datetime(year=year,
                        month=end_month,
                        day=calendar.monthrange(year, end_month)[1])
    return tuple([begin_date, end_date])


def account_balance_items(account_id, year=None, month=None, since_begin=False):
    # define required queryset filters
    queryset_filters = {'is_payed': True}

    # define date queryset filters
    if year is not None:
        if since_begin is True:
            date_filter = range_date_from_beginning(year, month=month)
        else:
            date_filter = range_date_specific(year, month=month)
        queryset_filters.update({'date__range': date_filter})

    # define queryset filters
    income_items = Income.objects.filter(account_id=account_id, **queryset_filters)
    expenses_items = Expense.objects.filter(account_id=account_id, **queryset_filters)
    tranfers_items = Transfer.objects.filter(Q(source_account_id=account_id) | Q(destination_account=account_id),
                                             **queryset_filters).annotate_transfer_indicators(account_id)

    # build a list with all items
    balance_items = list(income_items) + list(expenses_items) + list(tranfers_items)

    # sort by date and operation type
    sort_balance_items_by_date(balance_items)

    return balance_items


def account_total_balance(account_id, year=None, month=None):
    total_balance = 0.0
    for balance_item in account_balance_items(account_id,
                                              year=year, month=month,
                                              since_begin=True):
        if balance_item.operation == 'income':
            total_balance += balance_item.value

        elif balance_item.operation == 'expense':
            total_balance -= balance_item.value

        elif balance_item.operation == 'transfer' and balance_item.source_account_id == account_id:
            total_balance -= balance_item.value

        elif balance_item.operation == 'transfer' and balance_item.destination_account_id == account_id:
            total_balance += balance_item.value

    return total_balance
