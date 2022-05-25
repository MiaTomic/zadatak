from itertools import product
from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    slug = models.SlugField(unique=True, db_index=True, null=True)
    user = models.OneToOneField(User, on_delete= models.CASCADE, null= True, blank= True)
    name = models.CharField(max_length=50, null= True)
    email = models.EmailField(max_length=150, null= True)

    def __str__(self):
      return self.name

class Product(models.Model):
    name = models.CharField(max_length=50, null= True)
    price = models.FloatField()
    content = models.TextField(default= 0)
    priprema = models.TextField(default= 0)
    sastojci = models.TextField(default= 0)
    image = models.ImageField(null= True, blank= True)


    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url

class Order(models.Model):
    slug = models.SlugField(unique=True, db_index=True, null=True)
    customer = models.ForeignKey(Customer, on_delete= models.SET_NULL, blank= True, null= True)
    date_ordered = models.DateTimeField(auto_now_add= True)
    complete = models.BooleanField(default= False, null= True, blank= False)
    transaction_id = models.CharField(max_length=50, null= True)


    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total



class OrderItem(models.Model):
    slug = models.SlugField(unique=True, db_index=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank= True, null= True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank= True, null= True)
    quantity = models.IntegerField(default= 0, null= True, blank= True)
    date_added = models.DateTimeField(auto_now_add= True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

