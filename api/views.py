from rest_framework.views import APIView
from rest_framework.response import Response
from .engine import RepaymentOptimizer

class DebtOptimizeView(APIView):
    def post(self, request):
        # Extract data from request
        debts = request.data.get('debts', [])
        extra_budget = request.data.get('extra_monthly_budget', 0)
        strategy = request.data.get('strategy', 'avalanche')

        # Run our engine
        engine = RepaymentOptimizer(debts, extra_budget, strategy)
        result = engine.calculate()

        return Response({
            "status": "success",
            "data": result,
            "message": f"You will be debt-free in {result['months']} months."
        })