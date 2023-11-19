from django.shortcuts import render, redirect
from .models import Friend
from .forms import AddFriendForm
from django.contrib.auth.models import User
from datetime import date
from django.core.mail import send_mail
# Create your views here.

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
            request.user.username + " added you as their friend on " + date.today(),
            "stellarledger117@gmail.com",
            [u.email],
            fail_silently=False,
        )
            return redirect('viewFriend') 
    else:
        form = AddFriendForm(request.POST)
    return render(request, 'friend/new.html', {
        'form':form
    })

def add_debt(request, id):
    u = User.objects.get(id=id)
    friend = Friend.objects.get(user=request.user, friend_username=u.username)
    if request.method == 'POST':
        debt = request.POST.get('debt')
        credit = request.POST.get('credit')
        friend.debt += debt
        friend.credit += credit
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
            "Your debt/credit with" + request.user.username + "is calculated as" + 
            "debt = " + friend.debt + " credit = " + friend.credit,
            "stellarledger117@gmail.com",
            [u.email]
        )
    return render(request, 'friends/debt.html', context = {
        "friend" : friend
        })