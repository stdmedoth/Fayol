from rest_framework import serializers
from api.models import Products

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ["name", "main_price", "wheight", "supplier", "unit_qnt", "retail_qnt", "group", "observation", "timestamp", "updated", "user"]
