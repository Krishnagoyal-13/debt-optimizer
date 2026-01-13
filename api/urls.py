from django.urls import path
from .views import DebtOptimizeView

urlpatterns = [
    path('optimize/', DebtOptimizeView.as_view(), name='optimize_debt'),
]