from django.urls import path
from . import views

urlpatterns = [

    path('', views.port_security, name="port_security"),

]
