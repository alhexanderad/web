from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import index 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name="index"),   
    path('persona/', include('persona.urls', namespace='persona')), 
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)