from django.db import models

# Create your models here.

class Product(models.Model): #product class is inheriting methods from models.Model class
    title        = models.CharField(max_length=120) #max_length = REQUIRED
    description  = models.TextField(blank=True, null=True)
    price        = models.DecimalField(max_digits=1000,decimal_places=2)
    summary      = models.TextField(blank=False, null=False)
    featured = models.BooleanField() # null=True, or default=True



