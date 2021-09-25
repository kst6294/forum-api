from rest_framework import generics, authentication, permissions
from rest_framework.settings import api_settings

from api.user.serializers import UserSerializer

class CreateUserView(generics.CreateAPIView) :
    """ 새로운 사용자 생성을 위한 APIView"""
    
    serializer_class = UserSerializer