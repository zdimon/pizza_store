# Generated by Django 2.1.4 on 2018-12-07 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_pizza_name_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('name', models.CharField(default='', max_length=150, verbose_name='Name')),
                ('message', models.TextField(verbose_name='Message')),
                ('is_public', models.BooleanField(default=False)),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Pizza')),
            ],
        ),
    ]