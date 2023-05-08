from django.contrib import admin
from django.urls import path, include
from .views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('about', include('about.urls')),
    path('candidates', include('candidates.urls')),
    path('blog/', include('blog.urls')),
    path('contact', include('contact.urls')),
    path('job/', include('job_section.urls')),
    path('', include('administration.urls'))
]