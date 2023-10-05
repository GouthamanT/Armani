from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    imageURL = models.CharField(max_length=255)
    createdat = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    imageURL = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    createdat = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    createdat = models.DateTimeField(default=timezone.now)
