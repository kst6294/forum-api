from rest_framework import routers

from django.urls import path, include

from api.board.views import (
    CommentCreateAPIView, 
    CommentListAPIView,
    LikeCreateAPIView,
    LikeDestroyAPIView,
    QuestionViewSet
)

app_name = "board"

router = routers.DefaultRouter(trailing_slash=False)

router.register('/questions', QuestionViewSet, basename='question')

urlpatterns = [
    path('', include(router.urls)),
    path('/questions/<int:pk>/comments', CommentListAPIView.as_view(), name="comment-list"),
    path('/comments', CommentCreateAPIView.as_view(), name="comment-create"),
    path('/like/question', LikeCreateAPIView.as_view(), name="like"),
    path('/unlike/questions/<int:pk>', LikeDestroyAPIView.as_view(), name="unlike")
]