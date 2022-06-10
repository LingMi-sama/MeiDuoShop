from rest_framework import serializers
from apps.goods.models import SPU,Brand,GoodsCategory


# SPU序列化器
class SPUSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    brand_id = serializers.IntegerField()
    category1_id = serializers.IntegerField()
    category2_id = serializers.IntegerField()
    category3_id = serializers.IntegerField()

    class Meta:
        model = SPU
        # fields = '__all__'
        # 设置序列化排除字段
        exclude = ['category1','category2','category3']

# Brand品牌表序列化器
class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ['id','name']


# 分类序列化器
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = GoodsCategory
        fields = ['id','name']