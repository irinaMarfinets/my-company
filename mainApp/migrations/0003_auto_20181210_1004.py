# Generated by Django 2.1.3 on 2018-12-10 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_auto_20181210_0929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]