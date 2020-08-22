from django.db import models

# Create your models here.

class User(models.Model):

    name = models.CharField(max_length=254)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    adress = models.CharField(max_length=254)
    password = models.CharField(max_length=254)

    def __str__(self):
        return self.name

class Order(models.Model):

    user_id = models.ForeignKey('User', null=True, on_delete=models.SET_NULL)
    total_price = models.IntegerField()
    order_date = models.DateField()
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Products(models.Model):

    product_name = models.CharField(max_length=254)
    product_price = models.IntegerField()
    product_description = models.CharField(max_length=1000)
    product_type = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Order_Products(models.Model):

    order_id = models.ForeignKey('Order', null=True, on_delete=models.SET_NULL)
    product_id = models.ForeignKey('Products', null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name      