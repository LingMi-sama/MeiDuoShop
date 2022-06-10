from django.contrib.auth.backends import ModelBackend
from apps.users.models import User


class MeiduoModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username=username, is_staff=True)
        except:
            try:
                user = User.objects.get(mobile=username)
            except:
                return None

        if user.check_password(password):
            return user
        else:
            return None
