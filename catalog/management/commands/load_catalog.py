from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from catalog.models import Catalog

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        Catalog.objects.all().delete()
        print('Создаем каталог')

        root = Catalog.objects.create(name='Каталог', parent=None)

        juice = Catalog.objects.create(name='Соки', parent=root)

        Catalog.objects.create(name='Томатный', parent=juice)
        Catalog.objects.create(name='Апельсиновый', parent=juice)

        tee = Catalog.objects.create(name='Чай', parent=root)

        black_tee = Catalog.objects.create(name='Чай черный', parent=tee)
        green_tee = Catalog.objects.create(name='Чай зеленый', parent=tee)

        coffee = Catalog()
        coffee.parent = root
        coffee.name = 'Кофе'
        coffee.save()

        print('Done')