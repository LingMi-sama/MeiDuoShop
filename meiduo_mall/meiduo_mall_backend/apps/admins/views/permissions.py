from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import Permission,ContentType
from apps.admins.myserializers.permissions import PermissionSerializer, ContentTypeSerializer
from apps.admins.utils import PageNum


class PermissionView(ModelViewSet):
    serializer_class = PermissionSerializer
    pagination_class = PageNum
    permission_classes = [IsAdminUser]
    queryset = Permission.objects.all()

    #父类中没有权限表的操作
    def content_types(self ,request):
         data = ContentType.objects.all()
         ser =  ContentTypeSerializer(data, many= True)
         return  Response(ser.data)

    def simple(self ,request):

        return None