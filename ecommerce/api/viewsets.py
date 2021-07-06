from rest_framework import viewsets
from ecommerce.api import serializers
from produtos import models
'''from rest_framework import generics


class ProdutosLista(generics.ListCreateAPIView):
    queryset = produtos.objects.all()
    serializer_class = ProdutosSerializer'''


class ProdutoViewsets(viewsets.ModelViewSet):
    serializer_class = serializers.ProdutoSerializer
    queryset = models.Produto.objects.all()
