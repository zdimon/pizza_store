from django.db import models

# Create your models here.
#from decimal import Decimal
from .pizza import Pizza

class Order(models.Model):

    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)
    name = models.CharField(max_length=150, default='', null=True, blank=True)
    phone = models.CharField(max_length=150, default='', null=True, blank=True)
    address = models.CharField(max_length=150, default='', null=True, blank=True)
    def __str__(self):
        return '%s' % (pizza.name)