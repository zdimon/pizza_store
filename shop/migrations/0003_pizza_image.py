# Generated by Django 2.1.3 on 2018-12-04 15:13

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='image',
            field=sorl.thumbnail.fields.ImageField(default='', upload_to='pizza_img'),
            preserve_default=False,
        ),
    ]
