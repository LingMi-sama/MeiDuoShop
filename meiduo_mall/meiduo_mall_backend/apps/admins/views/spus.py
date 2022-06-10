from rest_framework.viewsets import ModelViewSet

from apps.admins.myserializers.spus import SPUSerializer,BrandSerializer,CategorySerializer
from apps.goods.models import SPU,Brand,GoodsCategory
from rest_framework.generics import ListAPIView
from apps.admins.utils import PageNum


# 获取SPU数据、保存SPU数据
class SPUView(ModelViewSet):
    # 指定当前视图处理数据默认使用的查询集
    queryset = SPU.objects.all()
    # 指定当前视图使用的模型类序列化器
    serializer_class = SPUSerializer
    # 指定分页器
    pagination_class = PageNum

    # get_queryset方法默认返回的是所有查询集数据，没有处理过滤
    # 但是业务要求如果传入keyword字段则需要过滤
    def get_queryset(self):
        keyword = self.kwargs.get('keyword')
        if keyword:
            return self.queryset.filter(name__contains=keyword)
        return self.queryset.all()


# （1）、获取品牌信息
# 该接口需要请求GET方法返回一个列表数据，因此我们使用ListAPIView视图快速实现
class SPUBrandView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

# (2)、获取一级分类信息
# 该接口通过get请求返回一级分类列表数据，因此我们使用ListAPIView视图快速实现
class ChannelCategorysView(ListAPIView):
    # 指定当前视图处理数据使用的查询集
    queryset = GoodsCategory.objects.all()
    # 指定当前视图使用的序列化器
    serializer_class = CategorySerializer

    def get_queryset(self):
        # 获取前端传过来的二级或三级分类id，查找出对应的分类信息返回
        pk = self.kwargs.get('pk')
        if pk:
            return self.queryset.filter(parent=pk)
        return self.queryset.filter(parent=None)