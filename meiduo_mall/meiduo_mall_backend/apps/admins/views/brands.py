from apps.admins.utils import PageNum
from apps.admins.myserializers.brands import BrandSerializer
from apps.goods.models import Brand
from rest_framework.viewsets import ModelViewSet


class BrandView(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    pagination_class = PageNum
