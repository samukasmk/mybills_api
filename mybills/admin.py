from django.contrib import admin
from mybills.models import Account, Expense, Income, Transfer


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'account_type')


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('description', 'value', 'date', 'account', 'is_payed')


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('description', 'value', 'date', 'account', 'is_payed')


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ('description', 'value', 'date', 'source_account', 'destination_account', 'is_payed')
