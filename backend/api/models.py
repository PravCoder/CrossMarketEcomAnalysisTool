from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from datetime import datetime



class User(AbstractUser):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]  # No username required

    tracked_products = models.ManyToManyField("Product", related_name="tracked_products", blank=True)

class Product(models.Model):
    title = models.CharField(max_length=200,null=True)
    price = models.FloatField(default=0,null=True,blank=True)
    UPC = models.CharField(max_length=200,null=True)
    website = models.CharField(max_length=200,null=True)
    url = models.CharField(max_length=1000,null=True)
    # stores product-objs of same UPC-code but different platform
    cross_products = models.ManyToManyField("Product", related_name="related_cross_products", blank=True)

