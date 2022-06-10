from rest_framework.generics import ListAPIView
from apps.goods.models import GoodsCategory
from apps.admins.myserializers.goodscategory import GoodsCategorySeriializers
from apps.admins.utils import PageNum


class SkuThereApiView(ListAPIView):
    queryset = GoodsCategory.objects.filter(subs=None)
    serializer_class = GoodsCategorySeriializers
    pagination_class = PageNum
