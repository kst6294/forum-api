from django.test import TestCase
from django.contrib.auth import get_user_model

from api.board import models


def sample_user(email="kst6294@gmail.com", password="123123"):
    """ 샘플 질문 작성자 생성 """
    return get_user_model().objects.create_user(email, password)

def sample_question(user, title="질문입니다", content="궁금한 내용이에요"):
    return models.Question.create(user=user, title=title, content=content)


class ModelTests(TestCase):

    def test_create_question_successful(self):
        """ 새로운 질문 작성 """

        title = "샘플 질문"
        content = "샘풀 질문 본문"
        user = sample_user()

        question = models.Question.objects.create(
            title=title,
            content=content,
            user=user
        )

        self.assertEqual(question.title, title)
        self.assertEqual(question.content, content)

