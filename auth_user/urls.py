from django.urls import path
from .views import *

urlpatterns=[
    path('',login_,name='login_'),
    path('register/',register,name='register'),
    path('forgotpass/',forgotpass,name='forgotpass'),
    path('profile/',profile,name='profile'),
    path('logout_/',logout_,name='logout_'),
    path('edit_profile/',edit_profile,name='edit_profile'),
]