from django.urls import path

from api.board.views import CommentCreateAPIView, LikeCreateAPIView, QuestionDetailAPIView, QuestionListCreateAPIView

app_name = "board"

urlpatterns = [
    path('/questions', QuestionListCreateAPIView.as_view(), name="question-list-create"),
    path('/questions/<int:pk>', QuestionDetailAPIView.as_view(), name="question-detail"),
    path('/comment', CommentCreateAPIView.as_view(), name="comment-create"),
    path('/like/question', LikeCreateAPIView.as_view(), name="like"),
]