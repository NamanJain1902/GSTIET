from django.urls import path
from loginout import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register_user, name="register_user"),
]
