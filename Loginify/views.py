from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello_world(request):
    return render(request, 'Loginify/hello_world.html')

def login(request):
    pass

def signup(request):
    pass
