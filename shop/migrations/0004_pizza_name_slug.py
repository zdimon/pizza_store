# Generated by Django 2.1.4 on 2018-12-07 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_pizza_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='name_slug',
            field=models.CharField(default='', max_length=150),
        ),
    ]