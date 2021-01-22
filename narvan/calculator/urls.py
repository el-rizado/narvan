from django.urls import path, include
from . import views

urlpatterns = [
    path('fibonacci/', views.fibonacci, name='fibonacci'),
    path('factorial/', views.factorial, name='factorial'),
    path('ackermann/', views.ackermann, name='ackermann'),

]
