from django.urls import path, include
from authentication.views import CustomerRegisterView,ServiceRegisterView, LoginView, LogoutView

urlpatterns = [
    path('customer-register/', CustomerRegisterView.as_view(), name='cregister'),
    path('service-register/', ServiceRegisterView.as_view(), name='sregister'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]