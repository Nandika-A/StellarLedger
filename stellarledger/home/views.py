from django.shortcuts import render
from report.models import Transaction, Category
from report.views import getExpenses, getSavings
# Create your views here.

def homepage(request): 
    total_expenses = []
    savings = []
    cat = {}
    if request.user.is_authenticated:
        cat = Category.objects.filter(user=request.user)
        for c in cat:
            txn = Transaction.objects.filter(user=request.user, category=c.category)
            e=getExpenses(txn)
            s=getSavings(txn)
            if s < 0:
                s = 0 

            total_expenses.append(e)
            savings.append(s)
            
    return render(request, 'home/homepage.html',{
        'expenses': total_expenses,
        'cat': cat,
        'savings': savings
    })
    
