from django.urls import path, include
from authentication.views import UsersViewset
from rest_framework import routers

router = routers.SimpleRouter()

router.register('users', UsersViewset, basename='users')

app_name='authentication'
urlpatterns = [
	path('', include(router.urls)),
]