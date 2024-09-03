from django.urls import path
from .views import (
    ServiceTypeListCreateView,
    ServiceTypeDetailView,
    ServiceListCreateView,
    ServiceDetailView,
)

urlpatterns = [
    path('service-types/', ServiceTypeListCreateView.as_view(), name='service-type-list-create'),
    path('service-types/<int:pk>/', ServiceTypeDetailView.as_view(), name='service-type-detail'),
    path('services/', ServiceListCreateView.as_view(), name='service-list-create'),
    path('services/<int:pk>/', ServiceDetailView.as_view(), name='service-detail'),
]