from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserCreateForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,update_session_auth_hash
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.forms import PasswordChangeForm
from .models import User,Friend_Request





def signupview(request):
    if request.method == "POST":
        form=UserCreateForm(request.POST)
        if form.is_valid():
            new_user=form.save()
            print('thanks for registering')
            print(new_user)
            new_user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'])
            login(request,new_user)
            return HttpResponse('loggeDIN')
        else:
            print(request.POST,form.errors)
            return render(request,'signup.html',{'form':form,'error':form.errors})
    else:
        form=UserCreateForm()
        return render(request,'signup.html',{'form':form})

def loginview(request):
    if request.method == "POST":
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            login(request,user)
            return HttpResponse('logge DIN')
        else:
            return HttpResponse('login UNSUCCESSFULL')
    else:
        return render(request,'login.html')
    
@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return HttpResponse('done')
    else:
        form =PasswordChangeForm(request.user)
        return render(request, 'change_password.html', {
        'form': form
        })

@login_required
@user_passes_test(lambda u: u.is_superuser)
def password_reset(request):
    if request.method == "POST":
        user=User.objects.get(username=request.POST['username'])
        user.set_password('default123')
        user.save()
        return HttpResponse('password reset')
    else:
        return render(request,'password_reset.html')



# MAKING FRIENDS



def homepage(request):
    if request.user.is_authenticated:
        allusers=User.objects.all()
        return render(request,'homepage.html',{'allusers':allusers})
    else:
        return render(request,'homepage.html')

@login_required
def all_friends(request):
    return render(request,'all_friends.html')

@login_required
def send_friend_request(request,userID):
    from_user=request.user
    to_user=User.objects.get(id=userID)
    friend_request,created=Friend_Request.objects.get_or_create(from_user=from_user,to_user=to_user)
    if created:
        return HttpResponse('friend request sent')
    else:
        return HttpResponse('friend request was already sent')

@login_required
def accept_friend_request(request,requestID):
    friend_request=Friend_Request.objects.get(id=requestID)
    if friend_request.to_user == request.user :
        friend_request.to_user.friends.add(friend_request.from_user)
        friend_request.from_user.friends.add(friend_request.to_user)
        friend_request.delete()
        return HttpResponse('friend request accepted')
    else:
        return HttpResponse('friend request not accepted')
            
@login_required
def friend_requests(request):
    all_friend_requests=Friend_Request.objects.filter(to_user=request.user)
    return render(request,'homepage.html',{'all_friend_requests':all_friend_requests})

@login_required
def delete_friend(request,friendID):
    friend=User.objects.get(id=friendID)
    me=request.user
    me.friends.remove(friend)
    friend.friends.remove(me)
    return HttpResponse('deleted')