from django.db import models

from django.contrib.auth.models import User
from django.forms import IntegerField

from store.models import Product

class Cart(models.Model):
    user = models.ForeignKey(User, related_name='cart', on_delete=models.CASCADE)
    item=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    size=models.CharField(max_length=50,blank=True,null=True)
    color=models.CharField(max_length=100,blank=True,null=True)
    purchased=models.BooleanField(default= False)
    createdate=models.DateField(auto_now_add=True)
    updatedate=models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.quantity} X {self.item}"

    def get_total(self):
        total=self.item.price*self.quantity
        float_total= format(total,'0.2f')
        return float_total

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    orderitems= models.ManyToManyField(Cart)
    ordered=models.BooleanField(default=False)
    created=models.DateField(auto_now_add=True)
    paymentId=models.CharField(max_length=250,blank=True,null=True)
    orderId=models.CharField(max_length=250,blank=True,null=True)

    def get_totals(self):
        total=0
        for order_item in self.orderitems.all():
            total += float(order_item.get_total())
        return total