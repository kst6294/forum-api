from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient

from api.board import models, serializers


CREATE_COMMENT_URL = reverse('board:comment-create')


def sample_user(email="kst6294@gmail.com", password="123123"):
    """ 샘플 질문 작성자 생성 """
    return get_user_model().objects.create_user(email, password)

def sample_question(user, title="sample title", content="sample content"):
    return models.Question.objects.create(user=user, title=title, content=content)


class CommentApiTests(TestCase):
    """ 댓글 API 테스트 """

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'title@tests.com',
            '123123',
        )

        self.question = sample_question(sample_user())

        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_create_comment(self):
        """ 댓글 생성 """

        payload = {
            "question" : self.question.id,
            "content" : "comment content"
            }

        res = self.client.post(CREATE_COMMENT_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)