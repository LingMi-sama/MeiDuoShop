from apps.goods.models import SpecificationOption, SPUSpecification
from rest_framework import serializers


# 规格序列化器
class SpecSerializer(serializers.ModelSerializer):
    class Meta:
        model = SPUSpecification
        fields = ['id', 'name']


# 选项序列化器
class OptionSerializer(serializers.ModelSerializer):
    spec = serializers.StringRelatedField()
    spec_id = serializers.IntegerField()

    class Meta:
        model = SpecificationOption
        fields = ['id', 'value', 'spec', 'spec_id']
