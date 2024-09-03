from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ServiceType, Service
from .serializers import ServiceTypeSerializer, ServiceSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class GetAllowAnyPostIsAuthenticated(AllowAny):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return IsAuthenticated().has_permission(request, view)
        return True

class ServiceTypeListCreateView(APIView):
    permission_classes = [GetAllowAnyPostIsAuthenticated]

    def get(self, request):
        service_types = ServiceType.objects.all()
        serializer = ServiceTypeSerializer(service_types, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.is_service:
            serializer = ServiceTypeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Customer does not have permission to add servicetype"}, status=status.HTTP_403_FORBIDDEN)

class ServiceTypeDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            service_type = ServiceType.objects.get(pk=pk)
            serializer = ServiceTypeSerializer(service_type)
            return Response(serializer.data)
        except ServiceType.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            service_type = ServiceType.objects.get(pk=pk)
            serializer = ServiceTypeSerializer(service_type, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ServiceType.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            service_type = ServiceType.objects.get(pk=pk)
            service_type.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ServiceType.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ServiceListCreateView(APIView):
    permission_classes = [GetAllowAnyPostIsAuthenticated]

    def get(self, request, *args, **kwargs):
        query = request.query_params.get('query', None)
        processed_services = []

        if query == 'lowtohigh':
            services = Service.objects.all().order_by('price')
            for service in services:
                discounted_price = service.price - (2 / 100 * service.price)
                service_data = {
                    'id': service.id,
                    'type': service.type.id,
                    'title': service.title,
                    'description': service.description,
                    'price': discounted_price,
                    'discount': service.discount,
                }
                processed_services.append(service_data)
            return Response(processed_services)

        elif query == 'hightolow':
            services = Service.objects.all().order_by('-price')
            for service in services:
                surcharge_price = service.price + (2 / 100 * service.price)
                service_data = {
                    'id': service.id,
                    'type': service.type.id,
                    'title': service.title,
                    'description': service.description,
                    'price': surcharge_price,
                    'discount': service.discount,
                }
                processed_services.append(service_data)
            return Response(processed_services)

        else:
            services = Service.objects.all()
            serializer = ServiceSerializer(services, many=True)
            return Response(serializer.data)

    def post(self, request):
        if request.user.is_service:
            serializer = ServiceSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(seller=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Customer does not have permission to add service"}, status=status.HTTP_403_FORBIDDEN)


class ServiceDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            service = Service.objects.get(pk=pk)
            serializer = ServiceSerializer(service)
            return Response(serializer.data)
        except Service.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            service = Service.objects.get(pk=pk)
            serializer = ServiceSerializer(service, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Service.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            service = Service.objects.get(pk=pk)
            service.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Service.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)