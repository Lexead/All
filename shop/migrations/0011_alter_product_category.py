# Generated by Django 3.2.8 on 2022-01-10 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.IntegerField(choices=[(1, 'Электроника')], max_length=30, null=True),
        ),
    ]
