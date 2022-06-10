from rest_framework import serializers
from apps.goods.models import GoodsChannel, GoodsChannelGroup, GoodsCategory


class GoodsChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsChannel
        fields = '__all__'


class GoodsChannelGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsChannelGroup
        fields = ['id', 'name']


class GoodsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = ['id', 'name']
