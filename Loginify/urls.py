from django.urls import path
from . import views

urlpatterns =[
    path('hello/',views.hello_world, name='hello'),
    path('login/',views.login, name='login'),
    path('signup/',views.signup, name='signup'),
]
