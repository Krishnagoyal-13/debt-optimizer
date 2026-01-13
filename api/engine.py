from decimal import Decimal

class RepaymentOptimizer:
    def __init__(self, debts, extra_budget, strategy='avalanche'):
        self.debts = debts
        self.extra_budget = Decimal(str(extra_budget))
        self.strategy = strategy

    def calculate(self):
        # LLD: Strategy Pattern - Sorting logic
        if self.strategy == 'avalanche':
            sorted_debts = sorted(self.debts, key=lambda x: x['interest_rate'], reverse=True)
        else:
            sorted_debts = sorted(self.debts, key=lambda x: x['balance'])

        months = 0
        total_interest = Decimal('0.00')
        # Deep copy balances to simulate
        balances = [Decimal(str(d['balance'])) for d in sorted_debts]

        while sum(balances) > 0 and months < 360:
            months += 1
            available_cash = self.extra_budget
            
            # Step 1: Accrue Interest & Pay Minimums
            for i, debt in enumerate(sorted_debts):
                if balances[i] <= 0: continue
                interest = balances[i] * (Decimal(str(debt['interest_rate'])) / 100 / 12)
                total_interest += interest
                balances[i] += interest
                
                pay = min(balances[i], Decimal(str(debt['min_payment'])))
                balances[i] -= pay

            # Step 2: Apply Extra Cash to Priority Debt
            for i in range(len(balances)):
                if balances[i] > 0:
                    extra = min(balances[i], available_cash)
                    balances[i] -= extra
                    available_cash -= extra
                    if available_cash <= 0: break

        return {"months": months, "interest": round(total_interest, 2)}