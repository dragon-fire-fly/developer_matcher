from django.test import TestCase, Client
from django.urls import reverse

from datetime import date, datetime
from app_user.models import User

# This testing file aims to test the following points:

# - User registration page loads correctly
# - login page loads correctly
# - User can submit form on registration page
# - new user is successfully created
# - feedback if account creation failure
# - user logged in after signup 
# - user redirected correctly to home page after signing up
# - user can sign up/in with google
# - user can sign up/in with github
# - user can log in with existing user
# - user receives feedback if login has failed (e.g. incorrect password)


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

        # Check that registration page loads successfully
        self.assertEqual(response.status_code, 200)

        # Check correct template is used for registration
        self.assertTemplateUsed(response, "app_user/register.html")

        # test POST request with data from form
        # test user can submit form on registration page
        response = self.client.post(
            self.url,
            data={
                "username": "user_created_for_testing_2",
                "email": "test@test.com",
                "password1": "T35tP@55w0rd",
                "password2": "T35tP@55w0rd",
            },
        )

        # check redirection following registration (302 status code)
        self.assertEqual(response.status_code, 302)
        # check user redirected correctly to home page after signing up
        self.assertRedirects(response, "/user/success/")
        # check if user was added to the database
        self.assertEqual(
            User.objects.count(), 2)

        # check for feedback if account creation failure

        # check user logged in after signup 

        # Check signup date is correctly added
        self.assertTrue(
            User.objects.get(
                username="user_created_for_testing_2"
            ).date_joined, datetime.now()
        )

        def test_user_login(self):
            # - user can log in with existing user
            self.client.force_login(user=user)
            # - user receives feedback if login has failed (e.g. incorrect password)
            pass

        def test_user_login_google(self):
            # - test user can sign up/in with google
            pass

        def test_user_login_github(self):
            # - test user can sign up/in with github
            pass


if __name__ == "__main__":
    unittest.main()
