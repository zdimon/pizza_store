from django.db import models
from django.conf import settings
from slugify import slugify
from sorl.thumbnail import ImageField
from decimal import Decimal
from sorl.thumbnail import get_thumbnail
from django.utils.safestring import mark_safe

class BasePizzaType(models.Model):

    TYPES = (
        ('cheese', 'Cheese'),
        ('chicken', 'Chicken'),
        ('mushroom', 'Mushroom')
    )
    type_pizza = models.CharField(verbose_name='Тип пицы', max_length=25, choices=TYPES, default='cheese')
    name = models.CharField(max_length=200)
    name_slug = models.CharField(max_length=150, default='')
    desc = models.TextField()
    image = ImageField(upload_to='pizza_img')
    cost = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal(0.00))
    def __str__(self):
        return "{}".format(self.name)


    @property
    def det_thumb_url(self):
        try:
            return get_thumbnail(self.image.path, '50x50', crop='center', quality=99).url 
        except:
            return ''

    @property
    def thumb(self):
        try:
            return mark_safe('<img src="/media/%s" />' % get_thumbnail(self.image.path, '50x50', crop='center', quality=99)) 
        except:
            return ''

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('detail', kwargs={'slug': self.name_slug})


    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(BasePizzaType, self).save(*args, **kwargs)

    class Meta:
        abstract = True

class CheesePizza(models.Model):
    class Meta:
        abstract = True


class ChickenPizza(models.Model):
    class Meta:
        abstract = True


class MushroomPizza(models.Model):
    class Meta:
        abstract = True



class PizzaType(BasePizzaType, CheesePizza, ChickenPizza, MushroomPizza):
    pass