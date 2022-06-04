from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/blog/', include('temp.urls')),
    path('api/v1/base-auth', include('rest_framework.urls')),
    # path('', index, name='index'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)