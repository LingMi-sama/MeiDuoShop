from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import Group ,Permission

from apps.admins.myserializers.group import GroupSerializer
from apps.admins.myserializers.permissions import PermissionSerializer
from apps.admins.utils import PageNum


class GroupView(ModelViewSet):
    serializer_class = GroupSerializer
    pagination_class = PageNum
    permission_classes = [IsAdminUser]
    queryset = Group.objects.all()

    def simple(self,request):
        #获取权限
        data = Permission.objects.all();
        ser = PermissionSerializer(data, many =True)
        return  Response(ser.data)