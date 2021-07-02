from rest_framework import viewsets
from ecommerce.api import serializers
from produtos import models


class ProdutoViewsets(viewsets.ModelViewSet):
    serializer_class = serializers.ProdutoSerializer
    queryset = models.Produto.objects.all()
