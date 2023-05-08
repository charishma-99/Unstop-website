from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('courses/', include('courses.urls')),
    path('jobs/', include('jobs.urls')),
    path('mentorships/', include('mentorships.urls')),
]  + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


