from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from api.board import serializers
from api.board.models import Question
from api.board.permissions import IsOwnerOrReadOnly


class QuestionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class QuestionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)