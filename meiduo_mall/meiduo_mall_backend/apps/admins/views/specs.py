from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from apps.admins.utils import PageNum
from apps.goods.models import SPUSpecification, SPU
from apps.admins.myserializers.specs import SpecsSerializer, SPUSerializer


# 规格管理视图 对商品的规格 进行增删改查
class SpecsView(ModelViewSet):
    """
    curd 一个方法全部搞定
    """
    queryset = SPUSpecification.objects.all()  # 查询的表格
    serializer_class = SpecsSerializer
    pagination_class = PageNum  # 使用分页器
    permission_classes = [IsAuthenticated]

    # admins/goods/simple
    def simple(self, requst):
        spus = SPU.objects.all()
        ser = SPUSerializer(spus, many=True)  # 进行序列化
        return Response(ser.data)
