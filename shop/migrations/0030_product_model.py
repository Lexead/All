# Generated by Django 3.2.8 on 2022-01-18 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0029_alter_product_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='model',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
