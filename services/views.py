from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ServiceType, Service
from .serializers import ServiceTypeSerializer, ServiceSerializer
from rest_framework.permissions import IsAuthenticated

class ServiceTypeListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        service_types = ServiceType.objects.all()
        serializer = ServiceTypeSerializer(service_types, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ServiceTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
    permission_classes = [IsAuthenticated]

    def get(self, request):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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