# Generated by Django 3.2.8 on 2022-01-14 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_alter_product_images'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': ['title']},
        ),
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.CharField(max_length=30, null=True),
        ),
    ]