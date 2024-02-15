from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.login, name='login'),
    path('reset/', views.reset, name='reset'),
    path('register/', views.register, name='register'),
    path('resetpass/', views.resetpass, name='resetpass'),
    path('bar/', views.bar),
    path('profile/', views.profile, name='profile'),
    path('feed/', views.feed, name='feed'),
    path('chat/', views.chat, name='chat'),
    path('friends/', views.friends, name='friends'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
