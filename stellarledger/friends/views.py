from django.shortcuts import render, redirect
from .models import Friend, Group, UserGroup
from .forms import AddFriendForm, AddGroupForm
from django.contrib.auth.models import User
from datetime import date
from django.core.mail import send_mail
from decimal import Decimal
from django.contrib import messages
from allauth.account.decorators import verified_email_required
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# Create your views here.

@verified_email_required
def view_friends(request):
    friend = Friend.objects.filter(user=request.user)
    return render(request, "friends/friends.html", context={
        'friend': friend
    })

def add_friend(request):
    if request.method == 'POST':
        form = AddFriendForm(request.POST)
        if form.is_valid():
            friend = form.cleaned_data['friend_username']
            objs = Friend.objects.filter(user=request.user)
            for o in objs:
                if o.friend_username == friend:
                    messages.set_level(request, messages.DEBUG)
                    messages.error(request, "One user can be added only once!")
                    return redirect('addfriend')
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            u = User.objects.get(username=friend)
            send_mail(
            "Added you as friend",
            request.user.username + " added you as their friend on " + str(date.today()),
            "stellarledger117@gmail.com",
            [u.email],
            fail_silently=False,
        )
            return redirect('viewFriend') 
    else:
        form = AddFriendForm(request.POST)
    return render(request, 'friends/new.html', {
        'form':form
    })

def add_debt(request, name):
    u = User.objects.get(username=name)
    friend = Friend.objects.get(user=request.user, friend_username=name)
    if request.method == 'POST':
        debt = Decimal(float(request.POST.get('debt')))
        credit = Decimal(float(request.POST.get('credit')))
        due_date = request.POST.get('due_date')
        friend.debt += debt
        friend.credit += credit
        friend.due_date=due_date
        if(friend.debt > friend.credit):
            friend.debt -= friend.credit
            friend.credit = 0
        else:
            friend.credit -= friend.debt
            friend.debt = 0
        friend.date = date.today()
        friend.save()
        u = User.objects.get(username=friend.friend_username)
        send_mail(
            "Summary of your debt settlement",
            "Debt/credit of " + request.user.username + " with "+ friend.friend_username + " is calculated as " + 
            "debt = " + str(friend.debt) + " credit = " + str(friend.credit),
            "stellarledger117@gmail.com",
            [u.email, request.user.email]
        )
        return redirect('viewFriend')
    return render(request, 'friends/debt.html', context = {
        "friend" : friend
        })

def notify(request, name):
    u = User.objects.get(username=name)
    friend = Friend.objects.get(user=request.user, friend_username=name)
    send_mail(
            "Summary of your debt settlement",
            "Debt/credit of " + request.user.username + " with "+ friend.friend_username + " is calculated as " + 
            "debt = " + str(friend.debt) + " credit = " + str(friend.credit) + ". Settle this before due date.",
            "stellarledger117@gmail.com",
            [u.email]
        )
    messages.set_level(request, messages.DEBUG)
    messages.error(request, "mail sent!")
    return redirect('viewFriend')

def add_group(request):
    if request.method == 'POST':
        form = AddGroupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            f = form.save(commit=False)
            f.save()
            group = Group.objects.get(name=name)
            g = UserGroup.objects.create(user=request.user, group=group)
            group.debt_paid_to = request.user.username
            group.save()
            g.save()
            return redirect('viewGroup') 
    else:
        form = AddGroupForm(request.POST)
    return render(request, 'friends/addgroup.html', {
        'form':form
    })

@verified_email_required
def view_groups(request):
    g = UserGroup.objects.filter(user=request.user)
    return render(request, "friends/viewgroup.html", context={
        'g': g
    })

@verified_email_required
def addtogroup(request, id):
    if request.method == 'POST':
        group=Group.objects.get(id=id)
        if request.user.username == group.debt_paid_to:
            name = request.POST.get('name')
            u = User.objects.get(username=name)
            g = UserGroup.objects.create(user=u, group=group)
            g.save()
            return redirect('viewGroup') 
        else:
            messages.set_level(request, messages.DEBUG)
            messages.error(request, "Only debtor can add members to their broadcast lists.")
            return redirect('viewGroup')
    return render(request, 'friends/addtogroup.html')

@verified_email_required
def viewgroupmem(request, id):
    g = Group.objects.get(id=id)
    u = UserGroup.objects.filter(group=g)
    return render(request, 'friends/viewmem.html', {
        'u': u
    })

def resolvegroupdebt(request, id):
    g = Group.objects.get(id=id)
    u = UserGroup.objects.get(group=g, user=request.user)
    debtor = User.objects.get(username=g.debt_paid_to)

    html_content = render_to_string('email_template.html',{"group" : g.name, "mem" : request.user, "amount": g.debt, 'urlpk': u.id})
    text_content = strip_tags(html_content)
    msg = EmailMultiAlternatives(
        'Debt settlement',
        request.user.username + " have settled their debt for the broadcast list " + g.name + ". Kindly approve or reject.",
        "stellarledger117@gmail.com",
        [debtor.email]
        )
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    
    return render(request, 'friends/resolve.html')

def updatedebt(request, id):
    if request.method == 'POST':
        group=Group.objects.get(id=id)
        debt = Decimal(float(request.POST.get('debt')))
        if request.user != group.debt_paid_to:
            messages.set_level(request, messages.DEBUG)
            messages.error(request, "Only debtor can edit group debt")
            return redirect('viewGroup')
        group.debt = debt
        group.save()
        return redirect('viewGroup') 
    return render(request, 'friends/updatedebt.html')

def approve(request, pk):
    u = UserGroup.objects.get(id=pk)
    if request.method == "POST":
        selected = request.POST.get('option')
        if selected == "approve":
            u.paid = "YES"
            u.save()
            send_mail(
                'resolved debt',
                u.user.username + " have resolved their debt for the broadcast list " + u.group.name,
                'stellarledger117@gmail.com',
                [request.user.email, u.user.email]
            )
        else:
            send_mail(
                'settlement rejected',
                    request.user.username + " have rejected your debt settlement for the broadcast list " + u.group.name,
                        'stellarledger117@gmail.com',
                        [request.user.email, u.user.email]
            )
        return redirect('home')
            
    return render(request, 'home/approve.html')
