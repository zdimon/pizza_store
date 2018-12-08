
from django.db import models

# Create your models here.
from decimal import Decimal
from sorl.thumbnail import ImageField
from sorl.thumbnail import get_thumbnail
from django.utils.safestring import mark_safe
from slugify import slugify
from .pizza_type_model import PizzaType

class Pizza(models.Model):
    SIZES = (
        ('big', 'Big'),
        ('middle', 'Middle'),
        ('small', 'Small'),
    )
    type = models.ForeignKey(PizzaType,on_delete=models.CASCADE)
    size = models.CharField(max_length=200, default='big', choices=SIZES)
    cost = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal(0.00))


    def __str__(self):
        return '%s (%s)' % (self.name,self.type)
