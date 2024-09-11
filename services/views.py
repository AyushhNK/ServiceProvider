from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Business
from .serializers import CategorySerializer, BusinessSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
# from .document import BusinessDocument

class GetAllowAnyPostIsAuthenticated(AllowAny):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return IsAuthenticated().has_permission(request, view)
        return True

class CategoryListCreateView(APIView):
    permission_classes = [GetAllowAnyPostIsAuthenticated]

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.is_service:
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "User does not have permission to add category"}, status=status.HTTP_403_FORBIDDEN)

class CategoryDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class BusinessListCreateView(APIView):
    permission_classes = [GetAllowAnyPostIsAuthenticated]

    def get(self, request, *args, **kwargs):
        query = request.query_params.get('query', None)
        processed_businesses = []

        if query == 'lowtohigh':
            businesses = Business.objects.all().order_by('price')
            for business in businesses:
                discounted_price = business.price - (2 / 100 * business.price)
                business_data = {
                    'id': business.id,
                    'type': business.type.id,
                    'name': business.name,
                    'description': business.description,
                    'price': discounted_price,
                    'discount': business.discount,
                }
                processed_businesses.append(business_data)
            return Response(processed_businesses)

        elif query == 'hightolow':
            businesses = Business.objects.all().order_by('-price')
            for business in businesses:
                surcharge_price = business.price + (2 / 100 * business.price)
                business_data = {
                    'id': business.id,
                    'type': business.type.id,
                    'name': business.name,
                    'description': business.description,
                    'price': surcharge_price,
                    'discount': business.discount,
                }
                processed_businesses.append(business_data)
            return Response(processed_businesses)

        else:
            businesses = Business.objects.all()
            serializer = BusinessSerializer(businesses, many=True)
            return Response(serializer.data)

    def post(self, request):
        if request.user.is_service:
            serializer = BusinessSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "User does not have permission to add business"}, status=status.HTTP_403_FORBIDDEN)

from django.conf import settings
class SearchByAddressOrCategoryView(APIView):
    def get(self, request):
        category = request.GET.get('category', None)
        address = request.GET.get('address', None)
        filters = {}
        if category:
            try:
                category_id = Category.objects.get(name=category).id
                filters['category'] = category_id
                print(settings.BASE_DIR)
            except Category.DoesNotExist:
                return Response({"error": "Category not found"}, status=404)
        if address:
            filters['address__icontains'] = address
            print(filters)
        businesses = Business.objects.filter(**filters)
        serializer = BusinessSerializer(businesses, many=True)
        return Response(serializer.data)



# class BusinessDetailView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, pk):
#         try:
#             business = Business.objects.get(pk=pk)
#             serializer = BusinessSerializer(business)
#             return Response(serializer.data)
#         except Business.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def put(self, request, pk):
#         try:
#             business = Business.objects.get(pk=pk)
#             serializer = BusinessSerializer(business, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Business.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def delete(self, request, pk):
#         try:
#             business = Business.objects.get(pk=pk)
#             business.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except Business.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        

# class BusinessSearchView(APIView):
#     def get(self, request):
#         query = request.query_params.get('q', None)
#         if query:
#             search_results = BusinessDocument.search().query("multi_match", query=query, fields=['name', 'description'])
#             businesses = [result.to_dict() for result in search_results]
#             return Response(businesses, status=status.HTTP_200_OK)
#         else:
#             return Response({"error": "No search query provided."}, status=status.HTTP_400_BAD_REQUEST)