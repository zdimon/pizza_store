from django.core.management.base import BaseCommand
from django.utils import timezone

from shop.models import Pizza

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        print('Поехали')
        for i in Pizza.types:
            p = Pizza()
            p.type = i[0]
            p.name = '%s pizza!' % i[1]
            p.cost = 10
            p.save()
            print('Creating %s' % i[0])
        print('Done')