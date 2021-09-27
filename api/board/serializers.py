from rest_framework import serializers
from rest_framework.response import Response

from api.board.models import Comment, Like, Question


class QuestionSerializer(serializers.ModelSerializer):
    """ 질문 시리얼라이저 """

    user = serializers.ReadOnlyField(source='user.name')

    class Meta:
        model = Question
        fields = ('id', 'user', 'title', 'content', 'created_at', 'updated_at',)
        ReadOnlyField = ('id', 'user', 'created_at', 'updated_at', )


    def create(self, validated_data):
        question = Question.objects.create(**validated_data, user=self.context['request'].user)
        question.save() 
        return question


class CommentSerializer(serializers.ModelSerializer):
    """ 댓글 시리얼라이저 """

    user = serializers.ReadOnlyField(source='user.name')

    class Meta:
        model = Comment
        fields = ('id', 'user', 'question', 'content', 'created_at', 'updated_at')
        ReadOnlyField = ('id', 'user', 'created_at', 'updated_at')


    def create(self, validated_data):
        comment = Comment.objects.create(**validated_data, user=self.context['request'].user)
        comment.save()
        return comment


class LikeSerializer(serializers.ModelSerializer):
    """ 좋아요 시리얼라이저 """
    user = serializers.ReadOnlyField(source='user.name')

    class Meta:
        model = Like
        fields = ('id', 'question', 'user',)  

    def create(self, validated_data):
        return Like.objects.create(**validated_data, user=self.context['request'].user)