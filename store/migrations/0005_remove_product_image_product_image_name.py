# Generated by Django 5.2.3 on 2025-07-04 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_product_image_alter_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='image_name',
            field=models.CharField(default='placeholder.jpg', max_length=255),
            preserve_default=False,
        ),
    ]
