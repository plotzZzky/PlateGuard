from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

import json


class LoginTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'temporary',
            'password': '1234x567'}
        self.client = APIClient()
        self.user = User.objects.create_user(**self.credentials)
        self.token = Token.objects.create(user=self.user)  # type:ignore
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.credentials_error = {'username': 'user_error', 'password': '12334555'}

    def test_login_status(self):
        response = self.client.post('/users/login/', self.credentials)
        self.assertEqual(response.status_code, 200)

    def test_login_content_type(self):
        response = self.client.post('/users/login/', self.credentials)
        try:
            j = json.loads(response.content)
        except Exception:
            j = False
        self.assertNotEqual(j, False)

    def test_login_content_result(self):
        response = self.client.post('/users/login/', self.credentials)
        result = json.loads(response.content)
        self.assertEqual(result['token'], self.token.key)

    def test_login_status_error(self):
        response = self.client.post('/users/login/', self.credentials_error)
        self.assertEqual(response.status_code, 300)

    def test_login_status_error_empty(self):
        response = self.client.post('/users/login/', {})
        self.assertEqual(response.status_code, 404)


class RegisterTest(TestCase):
    def setUp(self):
        self.username = 'newuser'
        self.email = 'newuser@mail.com'
        self.password = 12345678
        self.credentials = {
            'username': self.username,
            'email': self.email,
            'password1': self.password,
            'password2': self.password,
            'office': 'posto_01'
        }

    def test_register_status(self):
        response = self.client.post('/users/register/', self.credentials)
        self.assertEqual(response.status_code, 200)

    def test_register_check_token(self):
        response = self.client.post('/users/register/', self.credentials)
        user = User.objects.get(username=self.username)
        token = Token.objects.get(user=user)  # type: ignore
        result = json.loads(response.content)
        self.assertEqual(result['token'], token.key)

    def test_register_error_username(self):
        credentials = {
            'username': 'aaa',
            'email': self.email,
            'password1': self.password,
            'password2': self.password,
            'office': 'posto_01'
        }
        response = self.client.post('/users/register/', credentials)
        self.assertEqual(response.status_code, 300)

    def test_register_error_email(self):
        credentials = {
            'username': self.username,
            'email': 'email-mail-com',
            'password1': self.password,
            'password2': self.password,
            'office': 'posto_01'
        }
        response = self.client.post('/users/register/', credentials)
        self.assertEqual(response.status_code, 300)

    def test_register_error_pwd1(self):
        credentials = {
            'username': self.username,
            'email': self.email,
            'password1': '',
            'password2': self.password,
            'office': 'posto_01'
        }
        response = self.client.post('/users/register/', credentials)
        self.assertEqual(response.status_code, 300)

    def test_register_error_pwd2(self):
        credentials = {
            'username': self.username,
            'email': self.email,
            'password1': self.password,
            'password2': '',
            'office': 'posto_01'
        }
        response = self.client.post('/users/register/', credentials)
        self.assertEqual(response.status_code, 300)

    def test_register_error_pwd_diferent(self):
        credentials = {
            'username': self.username,
            'email': self.email,
            'password1': self.password,
            'password2': '1234x566',
            'office': 'posto_01'
        }
        response = self.client.post('/users/register/', credentials)
        self.assertEqual(response.status_code, 300)

    def test_register_error_pwd_7(self):
        credentials = {
            'username': self.username,
            'email': self.email,
            'password1': '1234567',
            'password2': '1234567',
            'office': 'posto_01'
        }
        response = self.client.post('/users/register/', credentials)
        self.assertEqual(response.status_code, 300)

    def test_register_error_no_office(self):
        credentials = {
            'username': self.username,
            'email': self.email,
            'password1': self.password,
            'password2': self.password,
            'office': ''
        }
        response = self.client.post('/users/register/', credentials)
        self.assertEqual(response.status_code, 300)

