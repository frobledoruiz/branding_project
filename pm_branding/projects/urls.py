# File created from scratch

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='projects-home'),
    path('about/', views.about, name='projects-about'),
]