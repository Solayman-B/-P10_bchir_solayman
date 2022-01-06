from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from authentication import views

app_name='authentication'
urlpatterns = [
    path('', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('signup/', views.signup_page, name = 'signup')
]