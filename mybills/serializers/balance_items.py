from rest_framework import serializers
from mybills.serializers.models import IncomeSerializer, ExpenseSerializer, TransferSerializer


class OperationSerializer(serializers.ModelSerializer):
    operation = serializers.CharField(read_only=True)
    operation_id = serializers.IntegerField(read_only=True)


class IncomeBalanceSerializer(IncomeSerializer, OperationSerializer):
    pass


class ExpenseBalanceSerializer(ExpenseSerializer, OperationSerializer):
    pass


class TransferBalanceSerializer(TransferSerializer, OperationSerializer):
    transfer_type = serializers.CharField(read_only=True)
    transfer_operator = serializers.CharField(read_only=True)


serializer_by_operation = {'income': IncomeBalanceSerializer,
                           'expense': ExpenseBalanceSerializer,
                           'tranfer': TransferBalanceSerializer}
