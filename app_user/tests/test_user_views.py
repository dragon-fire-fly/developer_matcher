from django.test import TestCase, Client
from django.urls import reverse
from datetime import date
from app_user.models import User


class TestUserRegistration(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="user_created_for_testing",
            password="T35tP@55w0rd",
            first_name="Test",
            last_name="User",
            email="test@test.com",
            date_joined=date(2023, 1, 1),
            github_username="test-user",
            github_url="https://github.com/testuser",
            linked_in="https://www.linkedin.com/in/test-user/",
            portfolio="https://www.test.com/",
        )

        # set up a client
        client = Client()

    def test_user_registration(self):
        # define url for registration page
        self.url = reverse("app_user:register")
        # Test GET route:
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

        # test POST request with data from form
        response = self.client.post(
            self.url,
            data={
                "username": "user_created_for_testing_2",
                "password": "T35tP@55w0rd",
                "first_name": "Test",
                "last_name": "User",
                "email": "test@test.com",
                "date_joined": date(2023, 1, 1),
                "github_username": "test-user",
                "github_url": "https://github.com/testuser",
                "linked_in": "https://www.linkedin.com/in/test-user/",
                "portfolio": "https://www.test.com/",
            },
        )

        # check redirection following registration (302 status code)
        self.assertEqual(response.status_code, 302)
        # check response.url is the correct page

        # check if user was added to the database
