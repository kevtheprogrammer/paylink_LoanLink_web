from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/test/', include('api.urls')), 
    path('dashboard/', include('core.urls')),
    path('user/', include('theme.urls')),
    # path("__reload__/", include("django_browser_reload.urls")),
]
  
urlpatterns += staticfiles_urlpatterns()