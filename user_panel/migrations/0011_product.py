# Generated by Django 3.2.4 on 2021-12-30 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0010_alter_profile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('categor', models.CharField(choices=[('Indoor', 'Indoor'), ('Outdoor', 'Outdoor'), ('Electronics', 'Electronics'), ('Mobiles', 'Mobiles')], max_length=200, null=True)),
                ('discription', models.CharField(default='', max_length=200)),
                ('image', models.ImageField(upload_to='product/')),
            ],
        ),
    ]