from django.contrib import admin
from .models import Debt

@admin.register(Debt)
class DebtAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'interest_rate', 'min_payment')
    search_fields = ('name',)