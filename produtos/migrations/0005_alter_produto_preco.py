# Generated by Django 3.2.5 on 2021-07-04 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0004_auto_20210702_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
