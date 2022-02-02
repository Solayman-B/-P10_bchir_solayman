from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from authentication.views import UserViewset
from rest_framework import routers

router = routers.SimpleRouter()

router.register('signup', UserViewset, basename='signup')

app_name='authentication'
urlpatterns = [
	path('', include(router.urls)),
	#path('', include('rest_framework.urls')),
	path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]