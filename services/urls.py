from django.urls import path
from .views import (
    CategoryListCreateView,
    CategoryDetailView,
    BusinessListCreateView,
    SearchByAddressOrCategoryView,
    ReviewAPIView,
    # BusinessDetailView,
    # BusinessSearchView
)

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('businesses/', BusinessListCreateView.as_view(), name='business-list-create'),
    path('search/', SearchByAddressOrCategoryView.as_view(), name='search-by-category'),
    path('business/<int:business_id>/reviews/', ReviewAPIView.as_view(), name='review-list-create'),
    path('reviews/<int:review_id>/', ReviewAPIView.as_view(), name='review-update-delete'), 
    # path('businesses/<int:pk>/', BusinessDetailView.as_view(), name='business-detail'),
    # path('search/', BusinessSearchView.as_view(), name='business-search'),
]