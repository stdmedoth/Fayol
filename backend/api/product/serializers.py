from rest_framework import serializers
from api.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "main_price", "wheight", "supplier", "unit_qnt", "retail_qnt", "group", "observation", "timestamp", "updated", "user"]
