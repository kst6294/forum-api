from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient

from api.board import models, serializers


LIST_CREATE_QUESTION_URL = reverse('board:question-list-create')


def detail_url(question_id):
    return reverse('board:question-detail', args=[question_id])

def sample_question(user, title="sample title", content="sample content"):
    return models.Question.objects.create(user=user, title=title, content=content)


class QuestionApiTests(TestCase):
    """ 질문 API 테스트 """

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'test@test.com',
            '123123',
        )
        
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_list_questions(self):
        """ 질문 목록 요청 """
        
        models.Question.objects.create(
            user=self.user,
            title="sample title",
            content="sample content"
        )

        models.Question.objects.create(
            user=self.user,
            title="sample title2",
            content="sample content2"
        )

        res = self.client.get(LIST_CREATE_QUESTION_URL)

        questions = models.Question.objects.all()
        serializer = serializers.QuestionSerializer(questions, many=True)
        
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_question(self):
        """ 질문 생성 """

        payload = {
            "title" : "test title",
            "content" : "test content"
        }

        res = self.client.post(LIST_CREATE_QUESTION_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
    
    def test_retrieve_post_detail(self):
        """ 질문 상세 확인 """

        question = sample_question(user=self.user)

        url = detail_url(question.id)

        res = self.client.get(url)

        serializer = serializers.QuestionSerializer(question)
        
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_update_post(self):
        """ 질문 수정 """

        payload = {
            "title" : "newtitle",        }

        question = sample_question(user=self.user)

        url = detail_url(question.id)

        res=self.client.patch(url)
        
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_delete_post(self):
        """ 질문 삭제 """

        question = sample_question(user=self.user)

        url = detail_url(question.id)

        res=self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)



