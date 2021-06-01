from django.contrib import admin
from django.urls import path
from app_django import views
urlpatterns = [
    path('usuario/',views.UserList.as_view()),
    path('post/',views.PostList.as_view()),

]
