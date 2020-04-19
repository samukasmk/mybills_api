from django.contrib import admin
from mybills.models import Account, Expense, Income, Transfer


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'account_type')
    list_filter = ('account_type',)


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('date', 'description', 'value', 'account', 'is_payed')
    list_filter = ('is_payed', 'date', 'account')


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('date', 'description', 'value', 'account', 'is_payed')
    list_filter = ('is_payed', 'date', 'account')


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ('date', 'description', 'value', 'source_account', 'destination_account', 'is_payed')
    list_filter = ('is_payed', 'date', 'source_account', 'destination_account')
