from api.board.tests.test_question_api import sample_question, sample_user
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.serializers import Serializer

from api.board.models import Like, Question
from api.board.serializers import LikeSerializer


LIKE_URL = reverse('board:like')


def unlike_url(question_id):
    return reverse('board:unlike', args=[question_id])

def sample_user(email="t1@t.com", password="112134"):
    return get_user_model().objects.create(email, password)

def sample_question(user, title="sample title", content="sample content"):
    return Question.objects.create(user=user, title=title, content=content)


class LikeApiTests(TestCase):
    """ Like API 테스트 """

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'test@test.com',
            '123123'
        )

        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_create_like(self):
        pass
        """ 질문에 like 요청 """
        user1 = get_user_model().objects.create(email="asdf@asdf.com", password="123123")

        question1 = Question.objects.create(user=user1)

        payload = {"question" : question1.id}

        res = self.client.post(LIKE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_delete_like(self):

        user1 = get_user_model().objects.create(email="asdf@asdf.com", password="123123")

        question1 = Question.objects.create(user=user1)

        Like.objects.create(question=question1, user=self.user)

        url = unlike_url(question1.id)

        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)