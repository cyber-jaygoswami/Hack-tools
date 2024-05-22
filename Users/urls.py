from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path("login",views.loginUser,name="LoginPage"),
    path("register",views.registerUser,name="RegisterPage"),
    path("feeback",views.feedback,name="FeedbackPage"),
    path("logout",views.logoutUser,name="logout"),
]