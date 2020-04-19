from django.db import models


class Income(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=350, null=True, blank=True)
    value = models.FloatField()
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    is_payed = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    operation = 'income'
    operation_id = 1

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f'{self.date}, {self.value}, {self.description}'

    def __getitem__(self, key):
        return getattr(self, key)

