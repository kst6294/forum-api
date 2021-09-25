from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_success(self):
        """ 이메일 사용자 생성 """

        email = "kst6294@gmail.com"
        password = "Password123!@#"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_new_user_email_normalized(self):
        """ 대문자로 입력했을 경우 소문자로 변경해서 사용자 확인 """

        email = "kst6294@GMAIL.COM"
        password = "Password123!@#"
        user = get_user_model().objects.create_user(
            email=email,
            password=password)

        self.assertEqual(user.email, email.lower())
        self.assertTrue(user.check_password(password))

    def test_create_new_user_invalid_email_fail(self):
        """ 사용자 생성시 잘못된 이메일로 요청한 경우 에러 발생"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Password123!@#')

    def test_create_new_superuser(self):
        """ 관리자 계정 생성 """
        
        user = get_user_model().objects.create_superuser(
            "kst6294@gmail.com",
            "Password123!@#"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

