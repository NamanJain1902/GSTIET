from django.urls import path
from ginfo import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add_scholar/', views.add_scholar, name="add_scholar"),
    path('scholars/', views.all, name="scholars_list"),
    path('<str:pk>/', views.profile, name="profile"),
]
