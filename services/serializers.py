from rest_framework import serializers
from .models import Category, Business

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name'] 

class BusinessSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Business
        fields = [
            'id', 
            'name',
            'description',
            'category',
            'address',
            'phone_number',
            'website',
            'email',
            'created_at',
            'updated_at',
        ]
