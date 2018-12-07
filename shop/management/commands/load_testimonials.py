from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from shop.models import Testimonial, Pizza
from django.core.files import File

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        print('Поехали')
        print('Deleting...')
        Testimonial.objects.all().delete()
        
        for p in Pizza.objects.all():
            for m in [1,2,3]:
                t = Testimonial()
                t.pizza = p
                t.message = 'Very good %s pizza!!!!' % p
                t.name = 'Dima'
                t.is_public = True
                t.email = 'dima@gmail.com'
                t.save()
           
                print('Creating %s' % p)
        print('Done')