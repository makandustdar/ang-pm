from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('ckeditor/', include('ckeditor_uploader.urls')),
                  path('adminbia2/', admin.site.urls),
                  path('', include('base.urls')),
                  path('users/', include('users.urls')),
                  path('review/', include('review.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
