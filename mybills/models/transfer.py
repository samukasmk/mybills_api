from django.db import models


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
