from django.test import TestCase, Client
from django.urls import reverse
from django.shortcuts import get_object_or_404

from app_user.models import User, Project, ProgramLang


class TestHomeViewGetViews(TestCase):
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
        # to be updated once home page has some content.
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

    def test_profile_detail_view_success(self):
        template = "app_home/user_detail_view.html"

        # show user profile of existing user
        url = reverse(
            "app_home:profile-detail-view", kwargs={"pk": self.user2.pk}
        )

        # force login of user1
        self.client.force_login(self.user1)
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template)
        # check that logged in user is user1
        self.assertEqual(response.context["user"], self.user1)
        # check that user of the viewed profile is user2
        self.assertEqual(response.context["user_for_profile"], self.user2)

    def test_profile_detail_view_not_found(self):
        # show 404 for profile of NONE existing user
        url = reverse("app_home:profile-detail-view", kwargs={"pk": 999})

        self.client.force_login(self.user1)
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

    def test_project_overview(self):
        # project overview when logged in
        self.client.force_login(self.user1)
        template = "app_home/project_overview.html"

        url = reverse("app_home:project-overview")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template)
        self.assertContains(response, self.project1.title)
        self.assertContains(response, self.project2.title)

    def test_project_overview_no_projects(self):
        # delete project1 and project2
        Project.objects.all().delete()

        self.client.force_login(self.user1)
        template = "app_home/project_overview.html"
        url = reverse("app_home:project-overview")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template)
        # check that project1 and 2 not in project overview
        self.assertNotContains(response, self.project1.title)
        self.assertNotContains(response, self.project2.title)
