from django.db import models
from django.conf import settings


class Question(models.Model):
    """ 질문데이터 모델 """
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "questions"


class Comment(models.Model):
    """ 댓글 모델 """
    content = models.CharField(max_length=120)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "comments"
