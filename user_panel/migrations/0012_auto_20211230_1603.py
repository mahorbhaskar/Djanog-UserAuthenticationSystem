# Generated by Django 3.2.4 on 2021-12-30 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0011_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='categor',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
