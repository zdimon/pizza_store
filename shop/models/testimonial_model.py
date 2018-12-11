
from django.db import models
from .pizza_type_model import PizzaType
from .managers import TestimonialManager


class Testimonial(models.Model):
    email = models.EmailField(verbose_name='Email', max_length=100)
    name = models.CharField(verbose_name='Name', max_length=150, default='')
    message = models.TextField(verbose_name='Message')
    is_public = models.BooleanField(default=False)
    pizza = models.ForeignKey(PizzaType,on_delete=models.CASCADE)

    objects = TestimonialManager()
    