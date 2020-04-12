from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from mybills.serializers import serializer_by_operation
from mybills.logic import account_balance_items, account_total_balance


class AccountBalanceList(APIView):
    def get(self, request, account_id, year=None, month=None):
        since_begin = request.GET.get('since_begin', '').lower() == 'true'

        model_items = account_balance_items(account_id, year=year, month=month, since_begin=since_begin)
        balance_items = []
        for model_item in model_items:
            serializer = serializer_by_operation[model_item.operation]
            serializer_item = serializer(model_item, context={'request': request}).data
            balance_items.append(serializer_item)
        return Response(balance_items, status=status.HTTP_200_OK)


class AccountTotalBalance(APIView):
    def get(self, request, account_id, year=None, month=None):
        total_balance_in_period = account_total_balance(account_id, year=year, month=month)
        return Response({'total': total_balance_in_period}, status=status.HTTP_200_OK)
