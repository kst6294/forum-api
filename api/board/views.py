from rest_framework import status, viewsets
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from api.board.serializers import CommentSerializer, QuestionSerializer, LikeSerializer
from api.board.models import Comment, Question, Like
from api.board.permissions import IsOwnerOrReadOnly
from api.board.filters import CustomSearchFilter


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    filter_backends = (CustomSearchFilter, )
    search_fiels = ('title', 'content')


class QuestionDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)


class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(question_id=self.kwargs['pk'])


class CommentCreateAPIView(CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)


class LikeCreateAPIView(CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (IsAuthenticated,)


class LikeDestroyAPIView(DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(question_id=self.kwargs['pk'])

    def delete(self, request, *args, **kwargs):
        if self.queryset.exists():
            self.queryset.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT) 
        return Response({"detail" : "You are not liked to this question"}, status=status.HTTP_400_BAD_REQUEST)
