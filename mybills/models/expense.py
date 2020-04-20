from django.db import models


class Expense(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=350, default='')
    value = models.FloatField()
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    is_payed = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    operation = 'expense'
    operation_id = 2

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f'{self.date}, {self.value}, {self.description}'

    def __getitem__(self, key):
        return getattr(self, key)
