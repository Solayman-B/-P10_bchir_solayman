from django.urls import path, include
from authentication.views import UsersViewset
from rest_framework import routers

router = routers.SimpleRouter()

router.register('signup', UsersViewset, basename='signup')

app_name='authentication'
urlpatterns = [
	path('', include(router.urls)),
]