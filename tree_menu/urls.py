from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about-page'),
    path('about/history/', views.history, name='history'),
    path('services/', views.services, name='services'),
    path('contacts/', views.contacts, name='contacts'),
    path('team/', views.team, name='team-page'),
]