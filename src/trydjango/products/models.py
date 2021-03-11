from django.db import models

# Create your models here.

class Product(models.Model): #product class is inheriting methods from models.Model class
    title        = models.CharField(max_length=120) #max_length = REQUIRED
    description  = models.TextField()
    price        = models.TextField()
    summary      = models.TextField(default="No free lunch! Just Dinner for two!")



