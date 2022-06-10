from rest_framework import serializers
from apps.users.models import User
import re


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "mobile", "email", "password")
        extra_kwargs = {
            'password': {
                'write_only': True,
                'max_length': 20,
                'min_length': 8,
            },
            'username': {
                'max_length': 20,
                'min_length': 5,
            },
        }

    # 父类的方法没有对密码加密
    def create(self, validated_data):
        # user =super().create(validated_data)
        # user.set_password(validated_data['password'])
        # user.save()
        user = User.objects.create_user(**validated_data)
        return user

    def validate_mobile(self, value):
        if not re.match(r'1[3-9]\d{9}', value):
            raise serializers.ValidationError('手机格式不对')
        return value
