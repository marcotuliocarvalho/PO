# Generated by Django 4.1.3 on 2022-11-22 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='quantity',
        ),
    ]
