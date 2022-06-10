from apps.goods.models import SpecificationOption, SPUSpecification
from apps.admins.myserializers.options import OptionSerializer, SpecSerializer
from rest_framework.viewsets import ModelViewSet
from apps.admins.utils import PageNum
from rest_framework.generics import ListAPIView


class OptionViewSet(ModelViewSet):
    queryset = SpecificationOption.objects.all()
    serializer_class = OptionSerializer
    pagination_class = PageNum


class SPUSpecListView(ListAPIView):
    queryset = SPUSpecification.objects.all()
    serializer_class = SpecSerializer
