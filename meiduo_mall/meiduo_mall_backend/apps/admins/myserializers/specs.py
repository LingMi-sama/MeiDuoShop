from rest_framework import serializers
from apps.goods.models import SPUSpecification, SPU


# 操作的是商品的规格表
class SpecsSerializer(serializers.ModelSerializer):
    # 指定关联外键的数据放回形式
    spu = serializers.StringRelatedField(read_only=True)
    spu_id = serializers.IntegerField()

    class Meta:
        model = SPUSpecification
        fields = "__all__"


# 返回SPU的字段信息
class SPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = SPU
        fields = "__all__"
