from django.urls import path
from power_monitoring_system_chart import views

urlpatterns = [
    path('', views.index, name='index'),
    path('power_monitor_chart/', views.power_monitor_chart, name='power_monitor_chart'),
]