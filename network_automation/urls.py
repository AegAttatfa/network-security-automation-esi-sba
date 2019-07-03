from django.urls import path, include
from django.contrib import admin


urlpatterns = [

    path('admin/', admin.site.urls),
    path('layer2/', include('layer2.urls')),
    path('', include('network_admin.urls')),

  ]