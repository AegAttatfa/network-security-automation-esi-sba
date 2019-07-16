from django.urls import path
from . import views

urlpatterns = [

    path('', views.port_security, name="port_security"),
    path('device/', views.device_list_view, name='device_list_view'),
    path('device/<str:hostname>/details', views.device_detail_view, name='device_detail'),
    path('device/<str:hostname>/interfaces', views.device_get_interfaces, name='device_get_interfaces'),

]
