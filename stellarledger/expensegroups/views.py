from django.shortcuts import render, redirect
from .models import Edge, ExpenseGraph, ExpenseGraphSolver, ExpenseGroup, ExpenseGroupMember
from .forms import AddExpenseGroupForm
from django.core.mail import send_mail
from decimal import Decimal
from django.contrib import messages
from allauth.account.decorators import verified_email_required
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.models import User
# Create your views here.

@verified_email_required
def view_expense_groups(request):
    g = ExpenseGroupMember.objects.filter(user=request.user)
    return render(request, 'expensegroups/view_expense_groups.html', {
        'g' : g
    })


def add_expense_group(request):
    if request.method == 'POST':
        form = AddExpenseGroupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            f = form.save(commit=False)
            f.save()
            group = ExpenseGroup.objects.get(name=name)
            g = ExpenseGroupMember.objects.create(user=request.user, group=group)
            g.save()
            return redirect('view_expense_groups') 
    else:
        form = AddExpenseGroupForm(request.POST)
    return render(request, 'friends/addgroup.html', {
        'form':form
    })


def add_members(request, id):
    if request.method == 'POST':
        group=ExpenseGroup.objects.get(id=id)
        name = request.POST.get('name')
        u = User.objects.get(username=name)
        g = ExpenseGroupMember.objects.create(user=u, group=group)
        g.save()
        return redirect('view_expense_groups') 
    return render(request, 'friends/addtogroup.html')

def add_txn(request, id):
    pass

def view_all_transactions(request, id):
    pass

def view_simplified_txns(request, id):
    pass

def edit_txn(request, id):
    pass

