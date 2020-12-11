from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import ProductSerializer
from .models import ProductField


class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductField.objects.all().order_by('message')
    serializer_class = ProductSerializer