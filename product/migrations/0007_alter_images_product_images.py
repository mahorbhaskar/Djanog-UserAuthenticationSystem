# Generated by Django 3.2.4 on 2022-01-04 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_images_product_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='product_images',
            field=models.ImageField(null=True, upload_to='product/images/'),
        ),
    ]
