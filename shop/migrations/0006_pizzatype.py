# Generated by Django 2.1.4 on 2018-12-08 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('big', 'Big'), ('middle', 'Middle'), ('small', 'Small')], default='big', max_length=200)),
                ('type_pizza', models.CharField(choices=[('cheese', 'Cheese'), ('chicken', 'Chicken'), ('mushroom', 'Mushroom')], default='cheese', max_length=25, verbose_name='Тип пицы')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]