from django.db import models


class Account(models.Model):
    class AccountType(models.TextChoices):
        CHECKING = 'checking', 'Checking account'
        SAVINGS = 'savings', 'Savings account'
        WALLET = 'wallet', 'Wallet'
        INVESTMENT = 'investments', 'Financial investments'
        OTHER = 'other', 'Other'

    name = models.CharField(max_length=300)
    account_type = models.CharField(max_length=50, default=AccountType.CHECKING, choices=AccountType.choices)
    description = models.CharField(max_length=350, default='')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def __getitem__(self, key):
        return getattr(self, key)
