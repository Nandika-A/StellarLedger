from django.shortcuts import render, redirect
from .models import Transaction, Category
from .forms import RecordTransactionForm, RecordCategoryForm
from datetime import date
from django.utils.timezone import timedelta

# Create your views here.

def recordTransaction(request):
    if request.method == 'POST':
        form = RecordTransactionForm(request.POST)
        if form.is_valid():
            to_or_from = form.cleaned_data['to_or_from']
            user_role = form.cleaned_data['user_role']
            amount = form.cleaned_data['amount']
            timestamp = form.cleaned_data['timestamp']
            category = form.cleaned_data['category']
            recurring = form.cleaned_data['recurring']
            form.save()
            transaction = Transaction.objects.create(user=request.user, to_or_from=to_or_from, user_role=user_role, amount=amount, timestamp=timestamp, category=category, recurring=recurring)
            transaction.save()
    else:
        form = RecordTransactionForm()
    
    return render(request, 'report/recordtransaction.html', {
        'form':form
    })

def createCategory(request):
    if request.method == 'POST':
        form = RecordCategoryForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            form.save()
            category = Category.objects.create(category=category)
            category.save()
    else:
        form = RecordCategoryForm()
    
    return render(request, 'report/recordcategory.html', {
        'form':form
    })

def deleteCategory(request, id):
    category = Category.objects.get(pk=id)
    category.delete()
    return redirect('viewCategories')

def viewCategory(request):
    category = Category.objects.filter(user=request.user)
    return render(request, 'report/viewcategories.html', {
        'categories':category
    })
    
def deleteTransaction(request, id):
    txn = Transaction.objects.get(pk=id)
    txn.delete()
    return redirect('viewTransaction')

def viewTransactions(request):
    if request.method == 'GET':
        time_filter = request.GET['time_filter']
        if time_filter == 'day':
            txn = Transaction.objects.filter(user=request.user, timestamp__gt=date.today() - timedelta(days=1))
        if time_filter == 'week':
            txn = Transaction.objects.filter(user=request.user, timestamp__gt=date.today() - timedelta(weeks=1))
        if time_filter == 'month':
            txn = Transaction.objects.filter(user=request.user, timestamp__gt=date.today() - timedelta(days=30))
        if time_filter == 'year':
            txn = Transaction.objects.filter(user=request.user, timestamp__gt=date.today() - timedelta(days=365))
    else:
        txn = Transaction.objects.filter(user=request.user)
    total_expenses=getExpenses(txn)
    savings=getSavings(txn)
    return render(request, 'report/viewtransactions.html', {
        'txn':txn,
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

def recurringbills(request):
    txn = Transaction.objects.filter(user=request.user, recurring='No')
    time_left = txn.timestamp
