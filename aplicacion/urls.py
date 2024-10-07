from django.contrib import admin
from django.urls import path
from .views import index,artistas

urlpatterns = [
    path('',index, name="index"),
    path('artistas',artistas, name="artistas"),
]