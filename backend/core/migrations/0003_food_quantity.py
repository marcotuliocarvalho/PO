# Generated by Django 4.1.3 on 2022-11-22 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_food_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]