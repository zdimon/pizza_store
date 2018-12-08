from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from shop.models import Pizza, PizzaType
from django.core.files import File

def load_pizza():
    print('Deleting...')
    Pizza.objects.all().delete()
    image_path = settings.BASE_DIR+'/data'
    for i in Pizza.types:
        img = '%s/%s.png' % (image_path,i[0])
        p = Pizza()
        p.type = i[0]
        p.name = '%s pizza!' % i[1]
        p.cost = 10
        p.save()
        p.image.save('%s.png' % p.id,File(open(img, 'rb')))
        print('Creating %s' % i[0])

def load_pizza_type():
    print('Deleting types...')
    PizzaType.objects.all().delete()    
    image_path = settings.BASE_DIR+'/data'
    for t in ['cheese','chicken','mushroom']:
        img = '%s/%s.png' % (image_path,t)
        pt = PizzaType()
        pt.type_pizza = t
        pt.name = '%s pizza!' % t
        pt.cost = 10
        pt.save()
        pt.image.save('%s.png' % pt.id,File(open(img, 'rb')))
        print('Creating %s' % t)

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        print('Поехали')
        load_pizza_type()
        print('Done')