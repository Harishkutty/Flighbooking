from django.urls import path
from .views import *

urlpatterns=[
    path('',home,name='home'),  
    path('book/<int:id>',book,name='book'),
    path('booking/',booking,name='booking'),
    path('history/',history,name='history'),
    path('profile/',profile,name='profile'),
    path('logout/',logout,name='logout'),
    path('support/',support,name='support'),
    path('about/',about,name='about'),
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    
    
    path('remove/<int:pk>',remove,name='remove'),
    path('hremove/<int:pk>',hremove,name='hremove'),
    
    
]