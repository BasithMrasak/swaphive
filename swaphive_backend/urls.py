# swaphive_backend/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/',     include('apps.auth_user.urls')),
    path('api/matching/', include('apps.matching.urls')),
    path('api/sessions/', include('apps.user_sessions.urls')),
    path('api/messages/', include('apps.messaging.urls')),
    path('api/dashboard/',include('apps.dashboard.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)