# Generated by Django 3.2.24 on 2024-03-17 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactus',
            options={'verbose_name': 'Contact Us', 'verbose_name_plural': 'Contact Us'},
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='phone',
        ),
    ]
