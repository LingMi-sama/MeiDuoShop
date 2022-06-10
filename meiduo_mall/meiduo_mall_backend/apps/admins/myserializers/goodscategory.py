from rest_framework import serializers
from apps.goods.models import GoodsCategory

class GoodsCategorySeriializers(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = ["id","name"]