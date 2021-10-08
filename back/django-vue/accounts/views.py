from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_layout
from .forms import SignupForm, LoginForm
from .models import Profile


def signup(request):
    if request.method == 'POST':    #signup함수가 request(POST)를 받게 되면
        form = SignupForm(request.POST, request.FILES)    
        if form.is_valid():
            user = form.save()
            return redirect('accounts:login')    #페이지를 accounts의 login로
        else:
            form = SignupForm()
        return render(request, 'accounts/signup.html', {
            'form'=form,    #form이라는 변수에 form을 담아 해당 주소로 이동
        })
    
def login_check(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        
        user = authenticate(username=username, password=pwd)
        
        if user is not None:
            login(redirect, user)
            return redirect('/')
        else:
            return render(request, 'accounts/login_fail_info.html')
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {
            'form'=form,
        })
    
def logout(request):
    django_logout(request)
    return redirect('/')
            



