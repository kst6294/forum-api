from rest_framework import generics, status
from rest_framework.mixins import DestroyModelMixin
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from api.board import serializers
from api.board.models import Comment, Question, Like
from api.board.permissions import IsOwnerOrReadOnly


class QuestionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):

        search = self.request.query_params

        # if 문 줄일 수 있는 방법 찾아보기...
        if search.get('title', None):
            return self.queryset.filter(title__icontains=search['title'])
        elif search.get('content', None):
            return self.queryset.filter(content__icontains=search['content'])
        else:
            return self.queryset.all()


class QuestionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """ 질문으로 filter 한 댓글 쿼리셋 """
        if self.kwargs['pk']:
            return self.queryset.filter(question_id=self.kwargs['pk'])
        return self.queryset


class LikeCreateAPIView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = serializers.LikeSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user, question_id=self.request.data.get('question'))
    
    def create(self, request, *args, **kwargs):
        if self.queryset.exists():
            self.queryset.delete()
            return Response(status.HTTP_204_NO_CONTENT)
        return super().create(request, *args, **kwargs)