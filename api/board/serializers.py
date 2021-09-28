from django.utils.translation import gettext as _

from rest_framework import serializers

from api.board.models import Comment, Like, Question


class CommentSerializer(serializers.ModelSerializer):
    """ 댓글 시리얼라이저 """

    user = serializers.ReadOnlyField(source='user.name')

    class Meta:
        model = Comment
        fields = ('id', 'user', 'question', 'content', 'created_at', 'updated_at')
        ReadOnlyField = ('id', 'user', 'created_at', 'updated_at')


    def create(self, validated_data):
        return Comment.objects.create(**validated_data, user=self.context['request'].user)


class QuestionSerializer(serializers.ModelSerializer):
    """ 질문 시리얼라이저 """

    user = serializers.ReadOnlyField(source='user.name')

    class Meta:
        model = Question
        fields = ('id', 'user', 'title', 'content', 'created_at', 'updated_at')
        ReadOnlyField = ('id', 'user', 'created_at', 'updated_at',)


    def create(self, validated_data):
        return Question.objects.create(**validated_data, user=self.context['request'].user)


class LikeSerializer(serializers.ModelSerializer):
    """ 좋아요 시리얼라이저 """
    user = serializers.ReadOnlyField(source='user.name')

    class Meta:
        model = Like
        fields = ('id', 'question', 'user',)  


    def create(self, validated_data):
        if Like.objects.filter(**validated_data, user=self.context['request'].user).exists():
            raise serializers.ValidationError(_('You are already liked to this question'))
        return Like.objects.create(**validated_data, user=self.context['request'].user)