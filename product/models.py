from enum import Flag
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    flag = models.SmallIntegerField(default=0)
    discription = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name

class Images(models.Model):
    product_images = models.ImageField(null=True, blank=False)
    flag = models.IntegerField(max_length=1, default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name