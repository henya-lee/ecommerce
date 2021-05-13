from django.db import models
from django.contrib.auth.models import User

from apps.store.models import Product

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.SET_NULL, blank=True, null=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    place = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    paid = models.BooleanField(default=False)
    paid_amount = models.FloatField(blank=True, null=True)

    def __str__(self):
        return '%s' % self.first_name

    def get_total_quantity(self):
        return sum(int(item.quantity) for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='item', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.DO_NOTHING)
    price = models.FloatField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return '%s' % self.id