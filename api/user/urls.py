from django.urls import path
from rest_framework.generics import CreateAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from api.user.views import CreateUserView


app_name = 'user'

urlpatterns = [
    path('/signup', CreateUserView.as_view(), name='signup'),
    path('/signin', TokenObtainPairView.as_view(), name='signin'),
    path('/token/refresh', TokenRefreshView.as_view(), name='token-refresh'),
    path('/token/verify', TokenVerifyView.as_view(), name='signin'),
]
