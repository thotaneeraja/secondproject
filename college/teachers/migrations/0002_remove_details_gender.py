# Generated by Django 4.0 on 2021-12-14 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='gender',
        ),
    ]