from rest_framework import serializers
from apps.goods.models import SKUImage, SKU


class ImagesSerializer(serializers.ModelSerializer):
    # sku_id = serializers.IntegerField
    class Meta:
        model = SKUImage
        # fields = '__all__'
        fields = ['id', 'sku', 'image']
