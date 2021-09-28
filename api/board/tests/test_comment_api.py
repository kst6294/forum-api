from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient

from api.board import models, serializers


CREATE_COMMENT_URL = reverse('board:comment-create')


def detail_url(question_id):
    return reverse('board:comment-list', args=[question_id])

def sample_user(email="kst6294@gmail.com", password="123123"):
    """ 샘플 질문 작성자 생성 """
    return get_user_model().objects.create_user(email, password)

def sample_question(user, title="sample title", content="sample content"):
    return models.Question.objects.create(user=user, title=title, content=content)


class CommentApiTests(TestCase):
    """ 댓글 API 테스트 """

    def setUp(self):
        self.question = sample_question(sample_user())
        self.user = get_user_model().objects.create_user(
            'title@tests.com',
            '123123',
        )
        
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

    def test_list_comments_on_question(self):
        """ 특정한 질문에 달려있는 댓글 보여주기 """

        question = sample_question(user=self.user)

        user2 = get_user_model().objects.create(email="asdf@asdf.com", password="qweasd")

        comment1 = models.Comment.objects.create(user=user2, question=question, content="tttt")
        comment2 = models.Comment.objects.create(user=user2, question=question, content="asdf")

        url = detail_url(question.id)
        res = self.client.get(url)

        comments = models.Comment.objects.filter(question=question)

        serializer = serializers.CommentSerializer(comments, many=True)
        
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
