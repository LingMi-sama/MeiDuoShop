from rest_framework.generics import ListAPIView
from apps.admins.utils import PageNum
from apps.admins.myserializers.channels import GoodsChannelSerializer, GoodsCategorySerializer, \
    GoodsChannelGroupSerializer
from apps.goods.models import GoodsChannel, GoodsCategory, GoodsChannelGroup
from rest_framework.viewsets import ModelViewSet


class GoodsChannelView(ModelViewSet):
    queryset = GoodsChannel.objects.all()
    serializer_class = GoodsChannelSerializer
    pagination_class = PageNum


class GoodsChannelGroupView(ListAPIView):
    queryset = GoodsChannelGroup.objects.all()
    # 指定当前视图使用的序列化器
    serializer_class = GoodsChannelGroupSerializer


class GoodsCategoryView(ListAPIView):
    # 指定当前视图处理数据使用的查询集
    queryset = GoodsCategory.objects.all()
    # 指定当前视图使用的序列化器
    serializer_class = GoodsCategorySerializer
