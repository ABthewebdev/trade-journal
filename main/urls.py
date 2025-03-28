from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('entry/', views.entry, name='entry'),
    path('exit/', views.exit, name='exit'),
    path('trade/', views.trade, name='trade'),
    path('profile/', views.profile, name='profile'),
    path('strategies/<str:strategy>/', views.strategy, name='strategy'),
    path('<str:date_str>/', views.dates, name='dates'),
]