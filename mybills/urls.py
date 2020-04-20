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
                         AccountViewSet, AccountBalanceItems, AccountBalanceTotal)

router = routers.DefaultRouter()

router.register(r'expenses', ExpenseViewSet)
router.register(r'incomes', IncomeViewSet)
router.register(r'transfers', TransferViewSet)
router.register(r'accounts', AccountViewSet)

urlpatterns = [
    re_path('^', include(router.urls)),
    # list balance items
    path('accounts/<int:account_id>/balance/items/', AccountBalanceItems.as_view()),
    path('accounts/<int:account_id>/balance/items/<int:year>/', AccountBalanceItems.as_view()),
    path('accounts/<int:account_id>/balance/items/<int:year>/<int:month>/', AccountBalanceItems.as_view()),

    # list balance items
    path('accounts/<int:account_id>/balance/total/', AccountBalanceTotal.as_view()),
    path('accounts/<int:account_id>/balance/total/<int:year>/', AccountBalanceTotal.as_view()),
    path('accounts/<int:account_id>/balance/total/<int:year>/<int:month>/', AccountBalanceTotal.as_view()),
]
