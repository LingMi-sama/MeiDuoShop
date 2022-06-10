from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from apps.admins.myserializers.admin import AdminSerializer
from apps.admins.myserializers.group import GroupSerializer
from apps.admins.utils import PageNum
from apps.users.models import User
from django.contrib.auth.models import Group


class AdminView(ModelViewSet):
    serializer_class = AdminSerializer
    pagination_class = PageNum
    permission_classes = [IsAdminUser]
    queryset = User.objects.filter(is_staff=True)

    def simple(self, request):
        data = Group.objects.all()
        ser = GroupSerializer(data, many=True)
        return Response(ser.data)
