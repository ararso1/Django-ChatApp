from . import views
from django.urls import path

urlpatterns = [
    path('', views.loginpage, name='loginpage'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.register, name='register'),
    path('chat', views.chat, name='chat'),
    path('post', views.post, name='post'),
    path('myaccount', views.myaccount, name='myaccount'),
    path('update_profile', views.update_profile, name='update_profile'),

]


