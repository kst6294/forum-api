from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('user:signup')
TOKEN_URL = reverse('user:signin')


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class UserApiTests(TestCase):
    """ User API Test """

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """ 회원가입 성공 """
        payload = {
            'email' : 'test@gmail.com',
            'password' : 'Password123!@#',
            'name' : 'Kim'
        }

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_exists(self):
        """ 회원가입 실패, 중복된 사용자 """
        payload = {
            'email' : 'kst6294@gmail.com',
            'password' : 'Password123!@#',
            'name' : 'Suntae Kim'
        }

        create_user(**payload)

        res = self.client.post(CREATE_USER_URL, payload)

        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue(user_exists)

    def test_password_too_short(self):
        """ 회원가입 실패, 적절하지 않은 비밀번호 """
        payload = {
            'email' : 'kst6294@gmail.com', 
            'password' : 'pw',
            'name' : 'suntae kim'
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    # def test_create_token_for_user(self):
    #     """ Test that a toekn is created for the user """
    #     payload = {
    #         'email' : 'kst6294@gmail.com',
    #         'password' : 'Password123!@#',
    #         'name' : 'suntaekim'
    #     }

    #     create_user(**payload)
    #     res = self.client.post(TOKEN_URL, payload)
        
    #     self.assertIn('token', res.data)
    #     self.assertEqual(res.status_code, status.HTTP_200_OK)
        
    # def test_create_token_invalid_credentials(self):
    #     """ Test that toekn is not created if invalid credentials are given """
    #     create_user(email='kst6294@gmail.com', password='Password123!@#')
    #     payload = {'email' : 'kst6294@gmail.com', 'password' : 'wrong'}
    #     res = self.client.post(TOKEN_URL, payload)

    #     self.assertNotIn('token', res.data)
    #     self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    # def test_create_token_no_user(self):
    #     """ Test that toekn is not created if user doesn't exist """
    #     payload = {'email' : 'kst6294@gmail.com', 'password' : 'pass'}
    #     res = self.client.post(TOKEN_URL, payload)

    #     self.assertNotIn('token', res.data)
    #     self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    # def test_create_token_missing_field(self):
    #     """ Test that email and password are required """
    #     payload = {'email' : 'kst6294', 'password' : ''}
    #     res = self.client.post(TOKEN_URL, payload)

    #     self.assertNotIn('token', res.data)
    #     self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)