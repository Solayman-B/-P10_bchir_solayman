from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('authentication.urls')),
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')),
    path('api-auth/', include('rest_framework.urls')),
]