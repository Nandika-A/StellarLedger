from django.shortcuts import render, redirect
from .models import Friend
from .forms import AddFriendForm
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