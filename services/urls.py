from django.urls import path
from .views import (
    CategoryListCreateView,
    CategoryDetailView,
    BusinessListCreateView,
    SearchByAddressOrCategoryView
    # BusinessDetailView,
    # BusinessSearchView
)

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('businesses/', BusinessListCreateView.as_view(), name='business-list-create'),
    path('search/', SearchByAddressOrCategoryView.as_view(), name='search-by-category')
    # path('businesses/<int:pk>/', BusinessDetailView.as_view(), name='business-detail'),
    # path('search/', BusinessSearchView.as_view(), name='business-search'),
]