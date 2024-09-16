from django.urls import path
from .views import GoogleLogin

urlpatterns = [
    path('google-login/', GoogleLogin.as_view(), name='google_login'),
]