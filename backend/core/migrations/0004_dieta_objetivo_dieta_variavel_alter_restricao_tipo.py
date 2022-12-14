# Generated by Django 4.1.3 on 2022-11-22 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_food_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='dieta',
            name='objetivo',
            field=models.IntegerField(choices=[(0, 'Maximizar'), (1, 'Minimizar')], default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dieta',
            name='variavel',
            field=models.IntegerField(choices=[(0, 'Carboidratos'), (1, 'Colesterol'), (2, 'Fibras'), (3, 'Kilocalorias'), (4, 'Proteínas'), (5, 'Açúcares'), (6, 'Gordura monossaturada'), (7, 'Gordura polissaturada'), (8, 'Gordura saturada'), (9, 'Lipídios'), (10, 'Calcio'), (11, 'Ferro'), (12, 'Sódio'), (13, 'Vitamina A IU'), (14, 'Vitamina A RAE'), (15, 'Vitamina B12'), (16, 'Vitamina B6'), (17, 'Vitamina C'), (18, 'Vitamina E'), (19, 'Vitamina K'), (20, 'Preço')], default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='restricao',
            name='tipo',
            field=models.IntegerField(choices=[(0, 'Carboidratos'), (1, 'Colesterol'), (2, 'Fibras'), (3, 'Kilocalorias'), (4, 'Proteínas'), (5, 'Açúcares'), (6, 'Gordura monossaturada'), (7, 'Gordura polissaturada'), (8, 'Gordura saturada'), (9, 'Lipídios'), (10, 'Calcio'), (11, 'Ferro'), (12, 'Sódio'), (13, 'Vitamina A IU'), (14, 'Vitamina A RAE'), (15, 'Vitamina B12'), (16, 'Vitamina B6'), (17, 'Vitamina C'), (18, 'Vitamina E'), (19, 'Vitamina K'), (20, 'Preço')]),
        ),
    ]
