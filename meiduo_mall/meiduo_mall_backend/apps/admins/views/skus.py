from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.goods.models import SKU, GoodsCategory, SPU
from apps.admins.myserializers.skus import SkuSerializers, GoodsCategorySerializer, SPUSpecificationSerializer
from apps.admins.utils import PageNum


class SkuAPIViewSet(ModelViewSet):
    # queryset = SKU.objects.all()
    def get_queryset(self):
        keyword = self.request.query_params.get('keyword')
        if keyword == '':
            return SKU.objects.all()
        elif keyword is None:
            return SKU.objects.all()
        else:
            return SKU.objects.filter(name__contains=keyword)

    serializer_class = SkuSerializers
    pagination_class = PageNum
    permission_classes = [IsAdminUser]

    @action(method=['get'], detail=False)
    def categories(self, request):
        data = GoodsCategory.objects.filter(subs__id=None)
        ser = GoodsCategorySerializer(data, many=True)
        return Response(ser.data)

    def specs(self, request, pk):
        #          sk sku表的id值
        spu = SPU.objects.get(id=pk)
        data = spu.specs.all()
        ser = SPUSpecificationSerializer(data, many=True)
        return Response(ser.data)
