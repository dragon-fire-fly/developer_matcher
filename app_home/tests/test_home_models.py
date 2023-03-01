from django.test import TestCase
from unittest import mock
from django.urls import reverse

from django.core.files.uploadedfile import SimpleUploadedFile

from app_user.models import (
    User,
    ProgramLang,
    Project,
    UserProfilePicture,
    ProjectPicture,
)


class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="testuser",
            password="@t3s7p4ss!",
            email="testuser@example.com",
            first_name="Test",
            last_name="User",
            location="",
            github_username="testuser",
            github_url="https://github.com/testuser",
            linked_in="https://www.linkedin.com/in/testuser",
            portfolio="https://testuser.github.io",
        )

        self.another_user = User.objects.create(
            username="anotheruser",
            password="4n0th3rp4ss",
            email="anotheruser@example.com",
            first_name="Another",
            last_name="User",
            location="",
            github_username="anotheruser",
            github_url="https://github.com/anotheruser",
            linked_in="https://www.linkedin.com/in/anotheruser",
            portfolio="https://anotheruser.github.io",
        )

        self.user.follows.add(self.another_user)
        self.another_user.follows.add(self.user)

        self.python = ProgramLang.objects.create(
            language="Python", language_icon=""
        )
        self.java = ProgramLang.objects.create(
            language="Java", language_icon=""
        )

        self.javascript = ProgramLang.objects.create(
            language="JavaScript", language_icon="path/to/javascript/icon.png"
        )

        self.user.p_language.add(self.python)
        self.user.p_language.add(self.java)

        self.project1 = Project.objects.create(
            title="Test Project 1",
            description="This is a test project 1",
        )

        self.project2 = Project.objects.create(
            title="Test Project 2",
            description="This is a test project 2",
        )

        self.project1.user.add(self.user)
        self.project1.p_language.add(self.python)

        self.project2.user.add(self.user, self.another_user)
        self.project2.p_language.add(self.python, self.javascript)

    def test_user_str_method(self):
        self.assertEqual(str(self.user), "<user: testuser>")

    def test_user_to_json_method(self):
        expected_output = {
            "username": "testuser",
            "full name": "Test User",
            "email": "testuser@example.com",
            "location": "",
            "github username": "testuser",
            "github url": "https://github.com/testuser",
            "linked in url": "https://www.linkedin.com/in/testuser",
            "portfolio url": "https://testuser.github.io",
        }
        self.assertEqual(self.user.to_json(), expected_output)

    def test_user_to_json_list_method(self):
        expected_output = {
            "programming languages": ["Python", "Java"],
            "p_language_icons": [
                "http://res.cloudinary.com/djlm3llv5/image/upload/p_language_icon",
                "http://res.cloudinary.com/djlm3llv5/image/upload/p_language_icon",
            ],
        }
        self.assertEqual(self.user.to_json_list(), expected_output)

    @mock.patch("cloudinary.uploader.upload")
    def test_user_profile_picture_model(self, cloudinary_field_mock):
        # mocking
        cloudinary_field_mock.return_value = "picture.jpg"
        # define URL & image
        mocked_picture = SimpleUploadedFile(
            "picture.jpg", b"file_content", content_type="image/jpeg"
        )

        profile_picture = UserProfilePicture.objects.create(
            user=self.user,
            profile_picture=cloudinary_field_mock.return_value,
        )

        self.assertEqual(
            profile_picture.profile_picture, cloudinary_field_mock.return_value
        )

    def test_project_model(self):
        self.assertEqual(str(self.project1), "<Project name: Test Project 1>")
        self.assertEqual(str(self.project2), "<Project name: Test Project 2>")
        self.assertEqual(self.project1.user.count(), 1)
        self.assertEqual(self.project1.p_language.count(), 1)
        self.assertEqual(self.project2.user.count(), 2)
        self.assertEqual(self.project2.p_language.count(), 2)

    @mock.patch("cloudinary.uploader.upload")
    def test_project_profile_picture_model(self, cloudinary_field_mock):
        # mocking
        cloudinary_field_mock.return_value = "picture.jpg"
        # define URL & image
        mocked_picture = SimpleUploadedFile(
            "picture.jpg", b"file_content", content_type="image/jpeg"
        )

        project_picture = ProjectPicture.objects.create(
            project=self.project1,
            project_picture=cloudinary_field_mock.return_value,
        )

        self.assertEqual(
            project_picture.project_picture, cloudinary_field_mock.return_value
        )
