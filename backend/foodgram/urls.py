from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from foodgram.settings import  MEDIA_URL, MEDIA_ROOT, STATIC_URL, STATIC_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('api/', include('api.urls')),
]

urlpatterns += static(
    MEDIA_URL, document_root=MEDIA_ROOT
)

urlpatterns += static(
    STATIC_URL, document_root=STATIC_ROOT
)