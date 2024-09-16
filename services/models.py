from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


User=get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='business_images/', default='business_images/default.png')

    def __str__(self):
        return self.name

class Business(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='businesses')
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    website = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='business_images/', default='business_images/default.png')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('business-detail', kwargs={'pk': self.pk})

class Review(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review for {self.business.name} by {self.user.username}'