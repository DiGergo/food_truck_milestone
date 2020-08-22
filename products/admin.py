from django.contrib import admin
from .models import User, Products, Order, Order_Products

# Register your models here.

admin.site.register(User)
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(Order_Products)