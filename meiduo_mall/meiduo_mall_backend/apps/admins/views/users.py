from rest_framework.generics import ListCreateAPIView

from apps.admins.myserializers.users import UserSerializer
from apps.admins.utils import PageNum
from apps.users.models import User

class UserListAPIView(ListCreateAPIView):

    # queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNum


    def get_queryset(self):
        if self.request.query_params.get('keyword') == '' :
            return  User.objects.all()
        else:
            return  User.objects.filter(username__contains=self.request.query_params.get('keyword'))