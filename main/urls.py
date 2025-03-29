from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('entry/', views.entry, name='entry'),
    path('exit/', views.exit, name='exit'),
    path('trade/', views.trade, name='trade'),
    path('profile/', views.profile, name='profile'),
    path('setups/<str:setup>/', views.setup, name='strategy'),
    path('options/', views.options, name='options'),
    path('<str:date_str>/', views.dates, name='dates'),
]