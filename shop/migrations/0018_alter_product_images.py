# Generated by Django 3.2.8 on 2022-01-11 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_alter_product_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ManyToManyField(related_name='products', to='shop.Image'),
        ),
    ]