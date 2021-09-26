from django.db.models import query
from django.db.models.query import QuerySet
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly

from api.board import serializers
from api.board.models import Comment, Question
from api.board.permissions import IsOwnerOrReadOnly


class QuestionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        """ 질문 검색 """

        keyword = self.request.query_params.get('keyword')
        queryset = self.queryset

        if keyword:
            queryset = queryset.filter(title__icontains=keyword)

        return queryset.all()


class QuestionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)


class CommentCreateAPIView(generics.CreateAPIView):
    QuerySet = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (IsAuthenticated,)