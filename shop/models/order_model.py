from django.db import models
from shop.tasks import order_process
# Create your models here.
#from decimal import Decimal
from .pizza_type_model import PizzaType

class Order(models.Model):

    pizza = models.ForeignKey(PizzaType,on_delete=models.CASCADE)
    def __str__(self):
        return '%s' % (pizza.name)
        
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        order_process.delay(self)
