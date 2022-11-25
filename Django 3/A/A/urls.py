from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# static(settings.MEDIA.URL, document_root=settings.MEDIA_ROOT) is only for development mode
# You can't use this on production mode
