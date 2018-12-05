from django.db import models

# Create your models here.
#from decimal import Decimal
from .pizza import Pizza

class Order(models.Model):

    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)
    def __str__(self):
        return '%s' % (pizza.name)