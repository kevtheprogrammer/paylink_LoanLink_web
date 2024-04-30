 
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/test/', include('api.urls')), 
    path('dashboard/', include('core.urls')),
  
]
  