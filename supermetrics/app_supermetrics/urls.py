from app_supermetrics import views
from django.urls import path

urlpatterns = [
    path('', views.dashboard, name=''),
    path('dashboard/', views.dashboard, name='dashboard'),
]
