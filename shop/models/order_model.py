from django.db import models

# Create your models here.
#from decimal import Decimal
from .pizza_type_model import PizzaType

class Order(models.Model):

    pizza = models.ForeignKey(PizzaType,on_delete=models.CASCADE)
    def __str__(self):
        return '%s' % (pizza.name)