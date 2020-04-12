from rest_framework import viewsets
from mybills.models import Income
from mybills.serializers import IncomeSerializer


class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    filterset_fields = ['account_id']
