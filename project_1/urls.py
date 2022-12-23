
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('project_1.common.urls')),
    path('user/', include('project_1.users.urls')),
    path('item/', include('project_1.items.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
