from rest_framework import viewsets
from mybills.models import Expense
from mybills.serializers.models import ExpenseSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    filterset_fields = ['account_id']
