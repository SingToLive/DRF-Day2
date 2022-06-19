from django.contrib import admin
from django.urls import path
from user import views


urlpatterns = [
    path('login/', views.UserApiView.as_view()),
    path('logout/', views.UserApiView.as_view()),
]