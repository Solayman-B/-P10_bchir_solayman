from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', include('authentication.urls')),
    path('content/', include('content.urls')),
    path('admin/', admin.site.urls),
]