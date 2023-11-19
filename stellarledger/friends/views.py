from django.shortcuts import render, redirect
from .models import Friend, Group, UserGroup
from .forms import AddFriendForm, AddGroupForm
from django.contrib.auth.models import User
from datetime import date
from django.core.mail import send_mail
from decimal import Decimal
from allauth.account.decorators import verified_email_required
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
    return redirect('viewFriend')

@verified_email_required
def add_group(request):
    if request.method == 'POST':
        form = AddGroupForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            return redirect('viewGroup') 
    else:
        form = AddFriendForm(request.POST)
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
        name = request.POST.get('name')
        u = User.objects.get(username=name)
        g = UserGroup.objects.create(user=u, group=group)
        g.save()
        return redirect('viewGroup') 
    return render(request, 'friends/addtogroup.html')

@verified_email_required
def viewgroupmem(request, id):
    g = Group.objects.get(id=id)
    u = UserGroup.objects.filter(group=g)
    return render(request, 'friends/viewmem.html', {
        'u': u
    })

# def resolvegroupdebt(request, id):
#     g = Group.objects.get(id=id)
#     u = UserGroup.objects.filter(group=g, user=request.user)
#     u.paid = "YES"
#     u.save()
#     return render()