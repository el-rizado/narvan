from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('fibonacci/<int:number>', views.fibonacci, name='fibonacci'),
    path('factorial/<int:number>', views.factorial, name='factorial'),

]
