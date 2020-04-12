from rest_framework import viewsets
from mybills.models import Transfer
from mybills.serializers import TransferSerializer


class TransferViewSet(viewsets.ModelViewSet):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
    filterset_fields = ['source_account_id', 'destination_account_id']
