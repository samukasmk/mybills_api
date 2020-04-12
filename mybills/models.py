from django.db import models


class Account(models.Model):
    class AccountType(models.TextChoices):
        CHECKING = 'Checking account'
        SAVING = 'Savings account'
        WALLET = 'Wallet'
        INVESTMENTS = 'Financial investments'
        OTHERS = 'Other'

    name = models.CharField(max_length=300, null=False, blank=False)
    account_type = models.CharField(max_length=50, null=False, blank=False,
                                    choices=AccountType.choices, default=AccountType.CHECKING)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __getitem__(self, key):
        return getattr(self, key)


class Income(models.Model):
    description = models.CharField(max_length=350, null=True, blank=True)
    value = models.FloatField(null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    account = models.ForeignKey('Account', null=True, blank=True, on_delete=models.CASCADE)
    is_payed = models.BooleanField(default=True, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    operation = 'income'
    operation_id = 1

    def __str__(self):
        return f'{self.date}, {self.value}, {self.description}'

    def __getitem__(self, key):
        return getattr(self, key)


class Expense(models.Model):
    description = models.CharField(max_length=350, null=True, blank=True)
    value = models.FloatField(null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    account = models.ForeignKey('Account', null=True, blank=True, on_delete=models.CASCADE)
    is_payed = models.BooleanField(default=True, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    operation = 'expense'
    operation_id = 2

    def __str__(self):
        return f'{self.date}, {self.value}, {self.description}'

    def __getitem__(self, key):
        return getattr(self, key)


class Transfer(models.Model):
    source_account = models.OneToOneField('Account', null=True, blank=True,
                                          on_delete=models.CASCADE, related_name='source_tranfers')
    destination_account = models.OneToOneField('Account', null=True, blank=True,
                                               on_delete=models.CASCADE, related_name='destination_tranfers')
    value = models.FloatField(null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    description = models.CharField(max_length=350, null=True, blank=True)
    is_payed = models.BooleanField(default=True, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    operation = 'tranfer'
    operation_id = 3

    def __str__(self):
        return (f'{self.date}, {self.value}, {self.description}, '
                f'source: {self.source_account}, dest: {self.destination_account}')

    def __getitem__(self, key):
        return getattr(self, key)
