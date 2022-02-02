# Generated by Django 3.2.8 on 2022-01-18 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_alter_image_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True)),
                ('logo', models.ImageField(default='...', upload_to='brand_images')),
            ],
        ),
        migrations.RenameModel(
            old_name='Image',
            new_name='ProductImage',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='image',
            new_name='icon',
        ),
        migrations.RemoveField(
            model_name='product',
            name='images',
        ),
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.productimage'),
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.brand'),
        ),
    ]
