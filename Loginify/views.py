import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from .serializers import UserDetailsSerializer
from .models import UserDetails
from .forms import LoginForm, SignupForm

# Create your views here.


def hello_world(request):
    return render(request, 'Loginify/hello_world.html')


def login(request):
    if request.method == 'POST':
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            email = loginForm.cleaned_data.get('email')
            password = loginForm.cleaned_data.get('password')
            try:
                userDetails = UserDetails.objects.get(
                    email=email, password=password)
                messages.success(request, f'Logged in as {email}')
                return redirect('login')
            except Exception as e:
                messages.error(request, 'Invalid email or password')
    else:
        loginForm = LoginForm()
    return render(request, 'Loginify/login.html', {'loginForm': loginForm})


def signup(request):
    if request.method == 'POST':
        signupForm = SignupForm(request.POST)
        if signupForm.is_valid():
            signupForm.save()
            messages.success(
                request, 'Account created successfully. Please log in.')
            return redirect('login')
    else:
        signupForm = SignupForm()
    return render(request, 'Loginify/signup.html', {'signupForm': signupForm})


def get_user_details(request):
    try:
        user_data = UserDetails.objects.all()
        serialized_data = UserDetailsSerializer(user_data, many=True)
        return JsonResponse(serialized_data.data, safe=False)
    except:
        return JsonResponse({"error": "Failed to fetch data"}, status=500)


def user_details(request):
    if request.method == 'GET':
        try:
            user_data = UserDetails.objects.all()
            serialized_data = UserDetailsSerializer(user_data, many=True)
            return JsonResponse(serialized_data.data, safe=False)
        except:
            return JsonResponse({"error": "Failed to fetch data"}, status=500)

    if request.method == 'POST':
        input_data = json.loads(request.body)
        serialized_data = UserDetailsSerializer(data=input_data)

        if serialized_data.is_valid():
            serialized_data.save()
            return JsonResponse(serialized_data.data, status=201)
        else:
            return JsonResponse(serialized_data.errors, status=400)


def user_details_by_email(request, email):
    if request.method == 'GET':
        try:
            user_data = UserDetails.objects.get(email=email)
            serialized_data = UserDetailsSerializer(user_data)
            return JsonResponse(serialized_data.data, safe=False)
        except:
            return JsonResponse({"error": "Failed to fetch data"}, status=500)

    if request.method == 'PUT':
        try:
            user_data = UserDetails.objects.get(email=email)
            input_data = json.loads(request.body)
            serialized_data = UserDetailsSerializer(user_data, data=input_data)

            if serialized_data.is_valid():
                serialized_data.save()
                return JsonResponse(serialized_data.data, status=200)
        except:
            return JsonResponse({"error": "Failed to update data"}, status=500)

    if request.method == 'DELETE':
        try:
            user_data = UserDetails.objects.get(email=email)
            user_data.delete()
            return JsonResponse({"message": "Data deleted successfully"}, status=204)
        except:
            return JsonResponse({"error": "Failed to delete data"}, status=500)

    if request.method == 'PATCH':
        try:
            user_data = UserDetails.objects.get(email=email)
            input_data = json.loads(request.body)
            serialized_data = UserDetailsSerializer(
                user_data, data=input_data, partial=True)
            if serialized_data.is_valid():
                serialized_data.save()
                return JsonResponse(serialized_data.data, status=200)
        except:
            return JsonResponse({"error": "Failed to update data"}, status=500)
