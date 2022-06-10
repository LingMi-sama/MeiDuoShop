from rest_framework import serializers
from apps.users.models import User


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    # 不满足
    def create(self, validated_data):
        user = super().create(validated_data)
        user.is_staff = True
        user.set_password(validated_data['password'])
        user.save()
        return user

    # 父类的修改方法不满足需求
    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
