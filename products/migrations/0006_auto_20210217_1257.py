# Generated by Django 3.1.6 on 2021-02-17 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_price_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price_list',
            name='product_id',
        ),
        migrations.DeleteModel(
            name='Colours',
        ),
        migrations.DeleteModel(
            name='Price_list',
        ),
    ]
