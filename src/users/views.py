from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserCreateForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login

# Create your views here.
# class SignUpView(CreateView):
#     form_class=UserCreateForm
#     success_url  = reverse_lazy('login')
#     template_name='registration/signup.html'

def homepage(request):
    return render(request,'homepage.html')

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