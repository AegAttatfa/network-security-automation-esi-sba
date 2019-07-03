from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [

    path('', views.dashboard, name='dashboard'),

    path('login/', auth_views.login, {'template_name': 'login.html'}, name='login'),
    path('logout/', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    path('logout/', auth_views.logout_then_login, name='logout_then_login'),

]
