# Generated by Django 3.2.8 on 2022-01-18 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0027_auto_20220119_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ManyToManyField(limit_choices_to=5, null=True, to='shop.ProductImage'),
        ),
    ]
