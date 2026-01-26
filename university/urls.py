from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect 

urlpatterns = [
    path('', lambda request: redirect('accounts/login/')), 
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.accounts.urls')),
    path('students/', include('apps.students.urls')),
    path('professors/', include('apps.professors.urls')),
    path('courses/', include('apps.courses.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)