from rest_framework import serializers

from .models import ProductField

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductField
        fields = ('message',)