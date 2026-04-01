from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .models import Character


class CharacterApiPermissionTests(APITestCase):
    def setUp(self):
        self.user_model = get_user_model()
        self.normal_user = self.user_model.objects.create_user(
            username='normal_user',
            password='password123',
            is_staff=False,
        )
        self.staff_user = self.user_model.objects.create_user(
            username='staff_user',
            password='password123',
            is_staff=True,
        )

        self.normal_token = Token.objects.create(user=self.normal_user)
        self.staff_token = Token.objects.create(user=self.staff_user)

        self.character = Character.objects.create(
            name='Test Character',
            gender='male',
            affiliation='Guild',
            homeland='City',
            occupation='Warrior',
            element='Fire',
            first_appearance='Episode 1',
            description='Test description',
        )

    def test_unauthenticated_user_cannot_access_character_list(self):
        response = self.client.get('/api/characters/')
        self.assertEqual(response.status_code, 401)

    def test_authenticated_user_can_read_character_list(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.normal_token.key}')
        response = self.client.get('/api/characters/')
        self.assertEqual(response.status_code, 200)

    def test_non_staff_user_cannot_create_character(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.normal_token.key}')
        response = self.client.post(
            '/api/characters/',
            {
                'name': 'Blocked Character',
                'gender': 'female',
            },
            format='json',
        )
        self.assertEqual(response.status_code, 403)

    def test_staff_user_can_create_character(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.staff_token.key}')
        response = self.client.post(
            '/api/characters/',
            {
                'name': 'Allowed Character',
                'gender': 'female',
            },
            format='json',
        )
        self.assertEqual(response.status_code, 201)
