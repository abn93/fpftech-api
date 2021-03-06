from rest_framework import serializers
from produtos import models


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Produto
        fields = ['id', 'nome', 'marca', 'categoria', 'preco']
