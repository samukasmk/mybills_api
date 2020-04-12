from django.db import models


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