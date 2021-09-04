from django.urls import path
from . import views
from analytics import views as analytics_view
from ginfo import views as ginfo_views
urlpatterns = [
    path('', views.index, name='index'),
    path('analytics/', analytics_view.index, name='analytics'),
    path('add_scholar/', ginfo_views.add_scholar, name='add_scholar'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('favourites/', views.favourites, name='favourites'),
    path('messages/', views.messages, name='messages'),
    path('settings', views.settings, name='settings'),
    path('delete_scholar/<str:pk>/', views.settings, name='delete_scholar'),
    path('edit_scholar/<str:pk>/', views.settings, name='edit_scholar'),
]
