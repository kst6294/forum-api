from django.db.models import query
from django.db.models.query import QuerySet

from rest_framework import generics, viewsets
from rest_framework.mixins import DestroyModelMixin
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from api.board import serializers
from api.board.models import Comment, Question, Like
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
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (IsAuthenticated,)


class LikeCreateAPIView(generics.ListCreateAPIView, DestroyModelMixin):
    queryset = Like.objects.all()
    serializer_class = serializers.LikeSerializer
    permission_classes = (IsAuthenticated,)
    

    # def get_queryset(self):
    #     return self.queryset.filter(
    #         user=self.request.user,
    #         question_id=self.request.data.get('question')
    #         )

    # def perform_create(self, serializer, *args, **kwargs):
    #     if self.get_queryset().exists():
    #         self.get_queryset().delete()
    #         return {}







        # question_id = self.request.data.get('question')
        # Like.objects.create(user=self.request.user, question=Question.objects.get(id=question_id))
        # print('11======================')
        # serializer.save(question_id=self.request.data.get('question'))

        # serializer.save(
        #     question_id=self.request.data.get('question')
        # )

# class LikeRetrieveAPIView(generics.RetrieveAPIView):
#     queryset = Like.objects.all()
#     serializer_class = serializers.LikeSerializer
#     permission_classes = (IsAuthenticated,)