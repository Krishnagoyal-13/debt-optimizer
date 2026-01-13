from django.db import models

class Debt(models.Model):
    """
    Represents a user's individual debt.
    Using DecimalField is a 'First Principles' choice to avoid floating-point errors.
    """
    name = models.CharField(max_length=100)
    balance = models.DecimalField(
        max_digits=12, 
        decimal_places=2, 
        help_text="Current outstanding balance"
    )
    interest_rate = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        help_text="Annual Interest Rate (APR) in percentage"
    )
    min_payment = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        help_text="Minimum required monthly payment"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # High-Level Design: Ordering helps in retrieval efficiency
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} (${self.balance})"