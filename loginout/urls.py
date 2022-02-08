from django.urls import path
from loginout import views

urlpatterns = [
    path("", views.index, name="index"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutMethod, name="logout"),
    path('register/', views.registerPage, name="register"),
]
