from django.test import TestCase, Client
from django.urls import reverse
from django.shortcuts import get_object_or_404

from app_user.models import User, Project, ProgramLang


class TestUserLogin(TestCase):
    def setUp(self):
        # create test users
        self.user1 = User.objects.create(
            username="user_created_for_testing",
            email="test@test.com",
            password="T35tP@55w0rd",
        )

        self.user2 = User.objects.create(
            username="user_created_for_testing2",
            email="test2@test2.de",
            password="T35tP@55w0rd2",
        )

        # create test projects
        self.project1 = Project.objects.create(
            title="ProjectTitle1",
            description="project description1",
        )

        self.project2 = Project.objects.create(
            title="ProjectTitle2",
            description="project description2",
        )

    def test_homeview_get(self):
        template = "app_home/index.html"
        url = reverse("app_home:index")

        # response when not logged in
        response = self.client.get(url)

        self.assertTemplateUsed(template)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please log in to continue")

        # response when logged in
        self.client.force_login(self.user1)
        response = self.client.get(url)

        self.assertTemplateUsed(template)
        self.assertEqual(response.status_code, 200)
        ## to be updated once home page has some content.
        self.assertNotContains(response, "Please log in to continue")

    def test_aboutview_get(self):

        template = "app_home/about.html"
        url = reverse("app_home:about")
        response = self.client.get(url)
        
        self.assertTemplateUsed(template)
        self.assertEqual(response.status_code, 200)

    def test_developeroverview_get(self):
        template = "app_home/developer_overview.html"
        url = reverse("app_home:developer-overview")
        response = self.client.get(url)

        # developer overview page when not logged in
        self.assertTemplateUsed(template)
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response, "Please log in or register to see other developers"
        )

        # developer overview page when logged in
        self.client.force_login(self.user1)
        response = self.client.get(url)
        self.assertNotContains(
            response, "Please log in or register to see other developers"
        )