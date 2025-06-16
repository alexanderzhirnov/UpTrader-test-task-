from django.contrib import admin
from django.urls import path
from tree_menu import views  # Импорт ваших views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about-page'),
    path('about/history/', views.history, name='history'),
    path('team/', views.team_page, name='team-page'),  # named URL
    path('services/', views.services, name='services'),  # named URL
    path('services/dev/', views.services_dev, name='dev'),
    path('contacts/', views.contacts, name='contacts'),
]