from rest_framework import serializers
from apps.orders.models import OrderInfo, OrderGoods
from apps.goods.models import SKU


class SKUSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKU
        fields = ['name', 'default_image']


class OrderGoodsSerializer(serializers.ModelSerializer):
    sku = SKUSerializer()

    class Meta:
        model = OrderGoods
        fields = ['count', 'price', 'sku']


class OrderSerializer(serializers.ModelSerializer):
    skus = OrderGoodsSerializer(many=True)
    class Meta:
        model = OrderInfo
        fields = "__all__"