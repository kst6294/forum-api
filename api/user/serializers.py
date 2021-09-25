from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.fields import ReadOnlyField


class UserSerializer(serializers.ModelSerializer):
    """ 사용자 모델 시리얼라이저"""

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'name', 'created_at', 'updated_at',)
        ReadOnlyField = ('created_at', 'updated_at')
        extra_kwargs = {'password' : {'write_only' : True, 'min_length' : 5}}

    def create(self, validated_data):
        """ 새로운 사용자 생성 """
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """ 사용자 정보 수정 """

        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user

