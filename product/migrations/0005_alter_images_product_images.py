# Generated by Django 3.2.4 on 2022-01-04 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='product_images',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
