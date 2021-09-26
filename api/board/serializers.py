from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from api.board.models import Comment, Question


class QuestionSerializer(serializers.ModelSerializer):
    """ 질문 시리얼라이저 """

    user = serializers.ReadOnlyField(source='user.name')

    class Meta:
        model = Question
        fields = ('id', 'user', 'title', 'content', 'created_at', 'updated_at')
        ReadOnlyField = ('id', 'user', 'created_at', 'updated_at')


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

