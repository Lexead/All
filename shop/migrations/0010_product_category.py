# Generated by Django 3.2.8 on 2022-01-10 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20220110_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[(1, 'Электроника')], max_length=30, null=True),
        ),
    ]
