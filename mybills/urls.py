"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path, include
from rest_framework import routers
from mybills.api import (ExpenseViewSet, IncomeViewSet, TransferViewSet,
                         AccountViewSet, AccountBalanceList, AccountTotalBalance)

router = routers.DefaultRouter()

router.register(r'expenses', ExpenseViewSet)
router.register(r'incomes', IncomeViewSet)
router.register(r'transfers', TransferViewSet)
router.register(r'accounts', AccountViewSet)

urlpatterns = [
    re_path('^', include(router.urls)),
    # list balance items
    path('balance/list/<int:account_id>/', AccountBalanceList.as_view()),
    path('balance/list/<int:account_id>/<int:year>/', AccountBalanceList.as_view()),
    path('balance/list/<int:account_id>/<int:year>/<int:month>/', AccountBalanceList.as_view()),

    # list balance items
    path('balance/total/<int:account_id>/', AccountTotalBalance.as_view()),
    path('balance/total/<int:account_id>/<int:year>/', AccountTotalBalance.as_view()),
    path('balance/total/<int:account_id>/<int:year>/<int:month>/', AccountTotalBalance.as_view()),
]