from django.urls import path

from api.board.views import CommentListCreateAPIView, LikeCreateAPIView, QuestionDetailAPIView, QuestionListCreateAPIView

app_name = "board"

urlpatterns = [
    path('/questions', QuestionListCreateAPIView.as_view(), name="question-list-create"),
    path('/questions/<int:pk>', QuestionDetailAPIView.as_view(), name="question-detail"),
    path('/questions/<int:pk>/comments', CommentListCreateAPIView.as_view(), name="comment-list"),
    path('/comments', CommentListCreateAPIView.as_view(), name="comment-create"),
    path('/like/question', LikeCreateAPIView.as_view(), name="like"),
]