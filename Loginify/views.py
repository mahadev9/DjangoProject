from django.shortcuts import render, redirect
from django.contrib import messages

from .models import UserDetails
from .forms import LoginForm, SignupForm

# Create your views here.


def hello_world(request):
    return render(request, 'Loginify/hello_world.html')


def login(request):
    if request.method == 'POST':
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            username = loginForm.cleaned_data.get('username')
            password = loginForm.cleaned_data.get('password')
            try:
                userDetails = UserDetails.objects.get(username=username, password=password)
                messages.success(request, f'Logged in as {username}')
                return redirect('login')
            except Exception as e:
                messages.error(request, 'Invalid username or password')
    else:
        loginForm = LoginForm()
    return render(request, 'Loginify/login.html', {'loginForm': loginForm})


def signup(request):
    if request.method == 'POST':
        signupForm = SignupForm(request.POST)
        if signupForm.is_valid():
            signupForm.save()
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('login')
    else:
        signupForm = SignupForm()
    return render(request, 'Loginify/signup.html', {'signupForm': signupForm})
