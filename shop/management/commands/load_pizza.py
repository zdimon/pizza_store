from django.core.management.base import BaseCommand
from django.utils import timezone

from shop.models import Pizza
from django.core.files import File
from django.conf import settings

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        print('Поехали')
        Pizza.objects.all().delete()
        image_path = settings.BASE_DIR+'/data'
        for i in Pizza.types:
            img = '%s/pizza.png' % image_path
            p = Pizza()
            p.type = i[0]
            p.name = '%s pizza!' % i[1]
            p.cost = 10
            p.save()
            p.image.save('%s.png' % p.id,File(open(img, 'rb')))
            print('Creating %s' % i[0])
        print('Done')