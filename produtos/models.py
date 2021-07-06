from django.db import models
from uuid import uuid4


class Produto(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10,
                                decimal_places=2)
