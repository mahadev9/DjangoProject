from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('user-details/', views.user_details, name='user_details'),
    path('user-details-by-email/<str:email>', views.user_details_by_email, name='user_details_by_email'),
]
