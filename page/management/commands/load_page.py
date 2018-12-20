from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from page.models import Page
from django.core.files import File

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        print('Создание страницы')
        p = Page()
        p.title = 'Заголовок'
        p.content = 'Содержание'
        p.name_slug = 'Алиас'
        p.meta_title = 'Мета-заголовок'
        p.meta_keywords = 'Мета-словосочитания'
        p.meta_description = 'Мета-описание'
        p.save()