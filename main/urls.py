from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('trade/', views.trade, name='trade'),
    path('<str:date>/', views.profile, name='profile'),
    path('entry/', views.entry, name='entry'),
    path('exit/', views.exit, name='exit'),
    path('dates/', views.dates, name='dates')
]