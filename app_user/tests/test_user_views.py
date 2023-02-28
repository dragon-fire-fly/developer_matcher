# from django.test import TestCase, Client
# from django.urls import reverse
# from django.shortcuts import get_object_or_404

# from datetime import date, datetime
# from app_user.models import User

# # This testing file aims to test the following points:

# # - User registration page loads correctly
# # - login page loads correctly
# # - User can submit form on registration page
# # - new user is successfully created
# # - feedback if account creation failure
# # - user logged in after signup
# # - user redirected correctly to home page after signing up
# # - user can sign up/in with google
# # - user can sign up/in with github
# # - user can log in with existing user
# # - user receives feedback if login has failed (e.g. incorrect password)


# class TestUserRegistration(TestCase):
#     def setUp(self):
#         # set up a client
#         client = Client()

#     def test_user_registration(self):
#         # Test number of users before form submission
#         self.assertEqual(User.objects.count(), 0)

#         # define url for registration page
#         self.url = reverse("app_user:register")

#         # Test GET route:
#         response = self.client.get(self.url)

#         # Check that registration page loads successfully
#         self.assertEqual(response.status_code, 200)

#         # Check correct template is used for registration
#         self.assertTemplateUsed(response, "app_user/register.html")

#         # test POST request with data from form
#         # test user can submit form on registration page


# #         response = self.client.post(
# #             self.url,
# #             data={
# #                 "username": "user_created_for_testing",
# #                 "email": "test@test.com",
# #                 "password1": "T35tP@55w0rd",
# #                 "password2": "T35tP@55w0rd",
# #             },
# #         )
# #         # check redirection following registration
# #         self.assertEqual(response.status_code, 302)

# #         # check user redirected correctly to user profile after signing up
# #         self.assertRedirects(response, "/user/profile/")

# #         # check if user was added to the database
# #         self.assertEqual(User.objects.count(), 1)

# #         newly_created_user = User.objects.get(
# #           username="user_created_for_testing"
# #           )
# #         # check user logged in and authenticated after signup
# #         self.assertTrue(newly_created_user.is_authenticated)

# #         # check signup date is correctly added
# #         self.assertTrue(newly_created_user.date_joined, datetime.now())

# #     def test_incorrect_user_registration(self):
# #         # Test number of users before form submission
# #         self.assertEqual(User.objects.count(), 0)

# #         # define url for registration page
# #         self.url = reverse("app_user:register")

# #         response = self.client.post(
# #             self.url,
# #             data={
# #                 "username": "user_created_for_testing",
# #                 "email": "test@test.com",
# #                 "password1": "T35tP@55w0rd",
# #                 "password2": "1nc0rr3ctT35tP@55w0rd",
# #             },
# #         )

# #         # test that no new user was created (number of users after
# #         # form submission)
# #         self.assertEqual(User.objects.count(), 0)

# #         # test that browser redirects back to the form for resubmission
# #         # self.assertEqual(response.status_code, 302)
# #         # self.assertRedirects(response, "/user/register/")

# #         # check for feedback if account creation failure


# # class TestUserLogin(TestCase):
# #     def setUp(self):
# #         self.user = User.objects.create(
# #             username="user_created_for_testing",
# #             password="T35tP@55w0rd",
# #             first_name="Test",
# #             last_name="User",
# #             email="test@test.com",
# #             date_joined=date(2023, 1, 1),
# #             github_username="test-user",
# #             github_url="https://github.com/testuser",
# #             linked_in="https://www.linkedin.com/in/test-user/",
# #             portfolio="https://www.test.com/",
# #         )
# #         # set up a client
# #         client = Client()
# #         self.client.logout()
# #         # define url for registration page
# #         self.url = "/user/login/"

# #     def test_user_login(self):

# #         # Test GET route:
# #         response = self.client.get(self.url)
# #         self.assertEqual(response.status_code, 200)
# #         self.assertTemplateUsed(response, "account/login.html")

# #         # Test POST route: user can log in with existing user
# #         response = self.client.post(
# #             self.url,
# #             data={
# #                 "username": "user_created_for_testing",
# #                 "password": "T35tP@55w0rd",
# #                 "password2": "T35tP@55w0rd",
# #             },
# #         )
# #         test_user = User.objects.get(username="user_created_for_testing")
# #         self.assertTrue(test_user.is_authenticated)

# #         # self.client.force_login(user=user)
# #         # - user receives feedback if login has failed
# #         # (e.g. incorrect password)

# #     def test_user_login_with_wrong_username(self):
# #         response = self.client.post(
# #             self.url,
# #             data={
# #                 "username": "user_not_created_for_testing",
# #                 "password": "T35tP@55w0rd",
# #                 "password2": "T35tP@55w0rd",
# #             },
# #         )

# #     def test_user_login_with_wrong_password(self):
# #         response = self.client.post(
# #             self.url,
# #             data={
# #                 "username": "user_created_for_testing",
# #                 "email": "test@test.com",
# #                 "password1": "T35tP@55w0rd",
# #                 "password2": "1nc0rr3ctT35tP@55w0rd",
# #             },
# #         )


# class TestGoogleLogin(TestCase):
#     def setUp(self):
#         pass

#     def test_user_login_google(self):
#         # test user can sign up/in with google
#         pass


# class TestGithubLogin(TestCase):
#     def setUp(self):
#         pass

#     def test_user_login_github(self):
#         # - test user can sign up/in with github
#         pass


# if __name__ == "__main__":
#     unittest.main()
