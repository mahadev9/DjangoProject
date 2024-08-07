from django.urls import path
from . import views

urlpatterns =[
    path('hello/',views.hello_world),
    path('login/',views.login),
    path('signup/',views.signup),
]
