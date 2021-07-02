# Generated by Django 3.2.5 on 2021-07-02 22:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id_produto', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome_produto', models.CharField(max_length=50)),
                ('marca_produto', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=50)),
                ('preco_produto', models.DecimalField(decimal_places=2, max_digits=4)),
                ('hora_resgistro_produto', models.DateField()),
            ],
        ),
    ]
