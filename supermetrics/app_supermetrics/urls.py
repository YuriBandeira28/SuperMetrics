from app_supermetrics import views
from django.urls import path

urlpatterns = [
    path('', views.dashboard, name=''),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('compras_dia', views.compras_dia, name='compras_dia'),
]
