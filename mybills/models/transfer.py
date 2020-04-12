from django.db import models
from django.db.models import When, Case, Value, CharField


class TransferQuerySet(models.QuerySet):
    def annotate_transfer_indicators(self, account_id):
        return self.annotate(
            transfer_operator=self.transfer_indicator_expr(
                account_id, dest_account_indicator='+', source_account_indicator='-')
        ).annotate(
            transfer_type=self.transfer_indicator_expr(
                account_id, dest_account_indicator='incoming', source_account_indicator='outgoing'))

    def transfer_indicator_expr(self, account_id, dest_account_indicator='+', source_account_indicator='-'):
        return Case(
            When(destination_account_id=account_id, then=Value(dest_account_indicator)),
            When(source_account_id=account_id, then=Value(source_account_indicator)),
            default=None,
            output_field=CharField())


class TransferManager(models.Manager):
    def get_queryset(self):
        return TransferQuerySet(self.model, using=self._db)


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

    objects = TransferManager()

    def __str__(self):
        return (f'{self.date}, {self.value}, {self.description}, '
                f'source: {self.source_account}, dest: {self.destination_account}')

    def __getitem__(self, key):
        return getattr(self, key)
