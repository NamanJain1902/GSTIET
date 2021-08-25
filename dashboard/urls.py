from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('analytics/', views.analytics, name='analytics'),
    path('add_scholar/', views.add_scholar, name='add_scholar'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('favourites/', views.favourites, name='favourites'),
    path('messages/', views.messages, name='messages'),
    path('settings', views.settings, name='settings'),
]
