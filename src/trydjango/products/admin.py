from django.contrib import admin

from .models import Product #relative import! Import the Product class from the models.py, since admin and models are from the same module!

admin.site.register(Product)
# Register your models here.
