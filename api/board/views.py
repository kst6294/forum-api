from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status, viewsets
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
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
    search_fiels = ('title',)
    # filterset_fields = ('title', 'content',)



# class QuestionListCreateAPIView(ListCreateAPIView):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#     search_fields = ('title', 'content',)

    # def get_queryset(self):

    #     search = self.request.query_params

    #     # if 문 줄일 수 있는 방법 찾아보기...
    #     if search.get('title', None):
    #         return self.queryset.filter(title__icontains=search['title'])
    #     elif search.get('content', None):
    #         return self.queryset.filter(content__icontains=search['content'])
    #     else:
    #         return self.queryset.all()


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
