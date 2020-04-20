from rest_framework import serializers
from mybills.models import Expense, Income, Transfer, Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
        ready_only_fields = ['created_at', 'updated_at']


class IncomeSerializer(serializers.ModelSerializer):
    operation = serializers.CharField(read_only=True)
    operation_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Income
        fields = '__all__'
        ready_only_fields = ['created_at', 'updated_at']


class ExpenseSerializer(serializers.ModelSerializer):
    operation = serializers.CharField(read_only=True)
    operation_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Expense
        fields = '__all__'
        ready_only_fields = ['created_at', 'updated_at']


class TransferSerializer(serializers.ModelSerializer):
    operation = serializers.CharField(read_only=True)
    operation_id = serializers.IntegerField(read_only=True)

    transfer_type = serializers.CharField(read_only=True)
    transfer_operator = serializers.CharField(read_only=True)

    class Meta:
        model = Transfer
        fields = '__all__'
        ready_only_fields = ['created_at', 'updated_at']


serializer_by_operation = {'income': IncomeSerializer,
                           'expense': ExpenseSerializer,
                           'tranfer': TransferSerializer}
