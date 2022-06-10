from rest_framework import serializers
from apps.goods.models import SKU, GoodsCategory, SPU, SPUSpecification, SpecificationOption, SKUSpecification

"""

caption:"浴霸不能"
category_id:115
cost_price:"6000"is_launched:"true"
market_price:"6000"
name:"iphone11"
price:"6000"
specs:[{spec_id: "4", option_id: 8}, {spec_id: "5", option_id: 12}]
spu_id:2
stock:"1"
"""


class SKUSpecificationSerializer(serializers.ModelSerializer):
    spec_id = serializers.IntegerField()
    option_id = serializers.IntegerField()

    class Meta:
        model = SKUSpecification
        fields = ['spec_id', 'option_id']


class SKUSerializer(serializers.ModelSerializer):
    # read_only 只在序列化(对象转换字典) 的时候使用,
    # 反序列化(字典转对象)忽略此字典
    spu = serializers.StringRelatedField(read_only=True)
    category = serializers.StringRelatedField(read_only=True)

    # 不添加的话  序列化器就不会为我们写入 spu_id 和 category_id
    # required
    # required 即可以获取数据,也可以写入数据
    spu_id = serializers.IntegerField()
    category_id = serializers.IntegerField()
    #
    specs = SKUSpecificationSerializer(many=True)

    class Meta:
        model = SKU
        fields = "__all__"

    def create(self, validated_data):

        # 1.写入sku
        if validated_data['specs']:
            specs = validated_data.get('specs')
            del validated_data['specs']

        from django.db import transaction

        with transaction.atomic():
            save_id = transaction.savepoint()
            try:
                sku = SKU.objects.create(**validated_data)

                # 2.写入sku对应的规格选项信息
                for spec in specs:
                    # spec = {"spce_id":4,"option_id":8}
                    SKUSpecification.objects.create(
                        sku=sku,
                        spec_id=spec.get('spec_id'),  # 规格id
                        option_id=spec.get('option_id')  # 选项id
                    )

                # 调用异步方法前,自己添加一个默认图片就号了
                sku.default_image = "group1/M00/00/02/CtM3BVrRdLGARgBAAAVslh9vkK00474545"
                sku.save()
            except Exception:
                transaction.savepoint_rollback(save_id)
            else:
                transaction.savepoint_commit(save_id)
                # 触发一个异步任务
                # from celery_tasks.html.tasks import generate_static_sku_detail_html
            # generate_static_sku_detail_html.delay(sku.id)

        return sku

    def update(self, instance, validated_data):

        # 1.先更新sku
        # instance.caption=validated_data.get('caption',instance.caption)
        # instance.category_id=validated_data.get('category_id',instance.category_id)
        # instance.save()
        # 判断是否存在,存在则先获取,再删除
        if validated_data['specs']:
            specs = validated_data.get('specs')
            del validated_data['specs']

        SKU.objects.filter(id=instance.id).update(**validated_data)

        # 2. 再更新specs 规格信息
        for spec in specs:
            SKUSpecification.objects.filter(sku_id=instance.id, spec_id=spec.get('spec_id')).update(
                spec_id=spec.get('spec_id'),
                option_id=spec.get('option_id')
            )

        return instance


class GoodsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = ['id', 'name']


class SPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = SPU
        fields = ['id', 'name']


###################SPU的规格###########################

class SpecificationOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecificationOption
        fields = '__all__'


class SPUSpecificationSerializer(serializers.ModelSerializer):
    options = SpecificationOptionSerializer(many=True)

    class Meta:
        model = SPUSpecification
        fields = '__all__'
