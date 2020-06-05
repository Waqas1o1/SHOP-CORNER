from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Default
    path('admin/', admin.site.urls),
    # This we work
    path('',include('Home.urls')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
