# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from shop.tasks import order_process

class Command(BaseCommand):

    def handle(self, *args, **options):
        print ('Test celery')
        order_process.delay()
        
