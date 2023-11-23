from django.shortcuts import render, redirect
from .models import Transaction, Category
from .forms import RecordTransactionForm, RecordCategoryForm
from datetime import date
from django.utils.timezone import timedelta
from allauth.account.decorators import verified_email_required

# Create your views here.
@verified_email_required
def recordTransaction(request):
    if request.method == 'POST':
        form = RecordTransactionForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect('viewTransaction') 
        
    else:
        form = RecordTransactionForm(request.POST)
    return render(request, 'report/recordtransaction.html', {
        'form':form
    })

@verified_email_required
def createCategory(request):
    if request.method == 'POST':
        form = RecordCategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('viewCategories') 
    else:
        form = RecordCategoryForm(request.POST)
    
    return render(request, 'report/recordCategory.html', {
        'form':form
    })

@verified_email_required
def deleteCategory(request, id):
    category = Category.objects.get(pk=id)
    category.delete()
    return redirect('viewCategories')

@verified_email_required
def viewCategory(request):
    category = Category.objects.filter(user=request.user)
    return render(request, 'report/viewcategories.html', {
        'categories':category
    })

@verified_email_required    
def deleteTransaction(request, id):
    txn = Transaction.objects.get(pk=id)
    txn.delete()
    return redirect('viewTransaction')

@verified_email_required
def viewTransactions(request):
    txn = Transaction.objects.filter(user=request.user)
    cat = Category.objects.filter(user=request.user)
    if request.method == 'GET':
        time_filter = request.GET.get('time_filter')
        if time_filter == 'day':
            txn = Transaction.objects.filter(user=request.user, timestamp__gt=date.today() - timedelta(days=1))
        if time_filter == 'week':
            txn = Transaction.objects.filter(user=request.user, timestamp__gt=date.today() - timedelta(days=7))
        if time_filter == 'month':
            txn = Transaction.objects.filter(user=request.user, timestamp__gt=date.today() - timedelta(days=30))
        if time_filter == 'year':
            txn = Transaction.objects.filter(user=request.user, timestamp__gt=date.today() - timedelta(days=365))
    total_expenses=getExpenses(txn)
    savings=getSavings(txn)
    if savings < 0:
        savings = 0
    return render(request, 'report/viewtransactions.html', {
        'txn':txn,
        'cat':cat,
        'expenses': total_expenses,
        'savings': savings
    })


def getExpenses(txn):
    # total amount debited = sum of debited only
    sum = 0
    for t in txn:
        if t.user_role == "sender":
            sum += t.amount

    return sum


def getSavings(txn):
    # amount earned - amount spent
    sum1 = 0
    sum2 = 0
    for t in txn:
        if t.user_role == "sender":
            sum1 += t.amount
        else:
            sum2 += t.amount
    
    return sum2-sum1

@verified_email_required
def changeTransactionCategory(request, id):
    txn = Transaction.objects.get(pk=id)
    cat = Category.objects.all()
    if request.method == 'POST':
        category = request.GET['category']
        txn.category=category
        txn.save()
    return render(request, 'report/changecategory.html', {
        'cat': cat
    })

@verified_email_required
def recurringbills(request):
    txn = Transaction.objects.filter(user=request.user, recurring='Yes', timestamp__gt=date.today())
    return render(request, 'report/reminder.html', {
        'txn': txn
    })  

def trackethereum(request):
    return render(request, 'home/eth.html')
