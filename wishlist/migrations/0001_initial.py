# Generated by Django 3.1.6 on 2021-02-19 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        ('products', '0007_product_colour'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_wishlist', to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wishlist', to='profiles.userprofile')),
                ('wishlist_products', models.ManyToManyField(through='wishlist.WishItems', to='products.Product')),
            ],
        ),
        migrations.AddField(
            model_name='wishitems',
            name='wishlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlist_items', to='wishlist.wishlist'),
        ),
    ]