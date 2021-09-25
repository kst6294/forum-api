from django.urls import path

from api.board.views import QuestionDetailAPIView, QuestionListCreateAPIView

app_name = "board"

urlpatterns = [
    path('/questions', QuestionListCreateAPIView.as_view(), name="question-list-create"),
    path('/questions/<int:pk>', QuestionDetailAPIView.as_view(), name="question-detail"),
]