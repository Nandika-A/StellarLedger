from django.shortcuts import render, redirect
from .models import Edge, ExpenseGraphSolver, ExpenseGroup, ExpenseGroupMember
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
        mem = ExpenseGroupMember.objects.filter(group=group)
        for m in mem:
            if m.user.username == name:
                messages.set_level(request, messages.DEBUG)
                messages.error(request, "Member already exists")
                return redirect('add_members')
        g = ExpenseGroupMember.objects.create(user=u, group=group)
        g.save()
        return redirect('view_expense_groups') 
    return render(request, 'friends/addtogroup.html')

def add_txn(request, id):
    group = ExpenseGroup.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        mem = ExpenseGroupMember.objects.filter(group=group)
        not_found = True
        for m in mem:
            if m.user.username == name:
                not_found = False
        if not_found:
            messages.error(request, "Not a group member")
            return redirect('add_txn')
        
        role = request.POST.get('role')
        amount = Decimal(float(request.POST.get('amount')))
        u = User.objects.get(username=name)
        if role == 'debtor':
            debtor = ExpenseGroupMember.objects.get(user=request.user, group=group)
            creditor = ExpenseGroupMember.objects.get(user=u, group=group)
        else:
            debtor = ExpenseGroupMember.objects.get(user=u, group=group)
            creditor = ExpenseGroupMember.objects.get(user=request.user, group=group)
        title = request.POST.get('title')
        
        obj = Edge.objects.create(group=group, debtor=debtor, creditor=creditor, amount=amount, title=title)
        obj.save()
        return redirect('view_expense_groups')

    return render(request, 'expensegroups/add_txn.html', {
        'group': group
    })

def view_all_transactions(request, id):
    group = ExpenseGroup.objects.get(id=id)
    edge = Edge.objects.filter(group=group)
    return render(request, 'expensegroups/view_all_transactions.html', {
        'edge': edge
    })

def view_simplified_txns(request, id):
    group = ExpenseGroup.objects.get(id=id)
    expense_graph_solver = ExpenseGraphSolver(group)
    expense_graph_solver.create_edges()
    txns = expense_graph_solver.get_transactions()
    transactions = []
    for t in txns:
        debtor = ExpenseGroupMember.objects.get(id=t['debtor'])
        creditor = ExpenseGroupMember.objects.get(id=t['creditor'])
        amount = t['amount']
        transactions.append({'debtor': debtor, 'creditor': creditor, 'amount': amount}) 
    return render(request, 'expensegroups/view_simplified_txns.html', {'transactions': transactions})