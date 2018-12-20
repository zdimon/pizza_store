from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField

class Page(models.Model):
    title = models.CharField(max_length=150, verbose_name=_(u'Заголовок'))
    content = RichTextField(verbose_name=_(u'Содержание'))
    name_slug = models.CharField(max_length=150, verbose_name=_(u'Алиас'))
    meta_title = models.CharField(max_length=150, verbose_name=_(u'Мета-заголовок'))
    meta_keywords = models.CharField(max_length=250, verbose_name=_(u'Мета-словосочитания'))
    meta_description = models.CharField(max_length=250, verbose_name=_(u'Мета-описание'))

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_page', kwargs={'pk': self.pk})
