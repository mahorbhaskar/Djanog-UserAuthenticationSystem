# Generated by Django 3.2.4 on 2021-12-22 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0006_auto_20211222_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=60, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='userquestionmodel',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_panel.question'),
        ),
    ]