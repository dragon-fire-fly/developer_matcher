from django.test import TestCase, Client
from django.urls import reverse
from unittest import mock
from django.shortcuts import get_object_or_404
from django.core.files.uploadedfile import SimpleUploadedFile

from app_user.models import User, Project, ProgramLang


class TestAppHomeViews(TestCase):
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

        # create test languages
        self.language1 = ProgramLang.objects.create(language="Python")
        self.language2 = ProgramLang.objects.create(language="HTML")

    def test_homeview_get(self):
        template = "app_home/index.html"
        url = reverse("app_home:index")

        # response when not logged in
        response = self.client.get(url)

        self.assertTemplateUsed(template)
        self.assertEqual(response.status_code, 200)

        # response when logged in
        self.client.force_login(self.user1)
        response = self.client.get(url)

        self.assertTemplateUsed(template)
        self.assertEqual(response.status_code, 200)
        # to be updated once home page has some content.
        self.assertContains(response, "Welcome")

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
            response, "Please log in or register to see the Developer Overview"
        )

        # developer overview page when logged in
        self.client.force_login(self.user1)
        response = self.client.get(url)
        self.assertTemplateUsed(template)
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(
            response, "Please log in or register to see other developers"
        )

    def test_profile_detail_view_success(self):
        template = "app_home/user_detail_view.html"
        # show user profile of existing user
        url = reverse(
            "app_home:profile-detail-view", kwargs={"pk": self.user2.pk}
        )

        # no user logged in
        response = self.client.get(url)
        # redirected to login page
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"/user/login/?next={url}")

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
        template = "app_home/project_overview.html"

        url = reverse("app_home:project-overview")
        response = self.client.get(url)

        # project overview page when not logged in
        self.assertTemplateUsed(template)
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response, "Please log in or register to see projects"
        )

        # project overview when logged in
        self.client.force_login(self.user1)
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

    def test_project_detail_view_project_exists(self):
        template = "app_home/project_detail_view.html"
        url = reverse(
            "app_home:project-detail-view", kwargs={"pk": self.project1.pk}
        )
        # no user logged in
        response = self.client.get(url)
        # redirected to login page
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"/user/login/?next={url}")

        # when user logged in
        self.client.force_login(self.user1)
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template)
        self.assertContains(response, self.project1.title)

    def test_project_detail_view_project_does_not_exist(self):
        template = "app_home/project_detail_view.html"
        url = reverse("app_home:project-detail-view", kwargs={"pk": 999})
        self.client.force_login(self.user1)
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

    def test_create_project_get(self):
        template = "app_home/create_project.html"
        url = reverse("app_home:create-project")

        # no user logged in
        response = self.client.get(url)
        # redirected to login page
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"/user/login/?next={url}")

        # user logged in
        self.client.force_login(self.user1)
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template)

    def test_create_project_post_valid(self):
        url = reverse("app_home:create-project")

        self.client.force_login(self.user1)
        # count number projects before new project creation
        project_count = Project.objects.count()
        # create new project
        response = self.client.post(
            url,
            {
                "title": "ProjectTitle3",
                "description": "Project description3",
                "p_language": [
                    self.language1.pk,
                    self.language2.pk,
                ],
            },
        )

        # Check that project was created successfully
        self.assertEqual(response.status_code, 302)
        # number of projects has increased by one
        self.assertEqual(Project.objects.count(), project_count + 1)
        # new project has correct title
        self.assertEqual(Project.objects.last().title, "ProjectTitle3")
        # check p langs have been added
        self.assertCountEqual(
            Project.objects.last().p_language.all(),
            [self.language1, self.language2],
        )
        # check new project belongs to logged in user
        self.assertEqual(Project.objects.last().user.last(), self.user1)

    def test_create_project_post_invalid(self):
        url = reverse("app_home:create-project")

        self.client.force_login(self.user1)
        # count number projects before new project creation
        project_count = Project.objects.count()
        # try to create new project without a title
        response = self.client.post(
            url,
            {
                "title": "",
                "description": "",
                "p_language": [
                    self.language1.pk,
                    self.language2.pk,
                ],
            },
        )

        # Check that project was NOT created
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Project.objects.count(), project_count)

    def test_edit_project_get(self):
        template = "app_home/edit_project.html"
        url = reverse(
            "app_home:project-edit-view", kwargs={"pk": self.project1.pk}
        )

        # no user logged in
        response = self.client.get(url)
        # redirected to login page
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"/user/login/?next={url}")

        # # user (NOT project owner)logged in
        # self.client.force_login(self.user2)
        # response = self.client.get(url)

        # self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, "app_home/project_overview.html")
        # self.assertRedirects(response, reverse("app_home:project-overview"))

        # Project owner logged in
        self.client.force_login(self.user1)
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template)

    def test_edit_project_post_valid(self):
        template = "app_home/edit_project.html"
        url = reverse(
            "app_home:project-edit-view", kwargs={"pk": self.project1.pk}
        )

        self.client.force_login(self.user1)
        # count no. projects before edit
        project_count = Project.objects.count()

        response = self.client.post(
            url,
            {
                "title": "CHANGED TITLE!",
                "description": "CHANGED Project description3",
                "p_language": [
                    self.language1.pk,
                    self.language2.pk,
                ],
            },
        )

        # test that project was changed successfully
        self.assertEqual(response.status_code, 302)
        # test number of projects has not changed
        self.assertEqual(Project.objects.count(), project_count)
        # test updated title
        self.assertEqual(
            Project.objects.get(pk=self.project1.pk).title, "CHANGED TITLE!"
        )
        # test updated description
        self.assertEqual(
            Project.objects.get(pk=self.project1.pk).description,
            "CHANGED Project description3",
        )
        # test that correct languages are saved
        self.assertCountEqual(
            Project.objects.get(pk=self.project1.pk).p_language.all(),
            [self.language1, self.language2],
        )

    def test_edit_project_post_invalid(self):
        template = "app_home/edit_project.html"
        url = reverse(
            "app_home:project-edit-view", kwargs={"pk": self.project2.pk}
        )

        self.client.force_login(self.user1)
        # count no. projects before edit
        project_count = Project.objects.count()

        # invalid data!
        response = self.client.post(
            url,
            {
                "title": "",
                "description": "CHANGED ONLY THIS!",
                "p_language": [],
            },
        )

        # Check that project is NOT changed!
        # reload page
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template)

        # prove data is unchanged!
        self.assertEqual(Project.objects.count(), project_count)
        self.assertEqual(
            Project.objects.get(pk=self.project2.pk).title, self.project2.title
        )
        self.assertEqual(
            Project.objects.get(pk=self.project2.pk).description,
            self.project2.description,
        )
        self.assertCountEqual(
            Project.objects.get(pk=self.project2.pk).p_language.all(),
            self.project2.p_language.all(),
        )

    def test_delete_project(self):
        template = "app_home/edit_project.html"
        url = reverse(
            "app_home:delete-project", kwargs={"pk": self.project1.pk}
        )

        # no user logged in
        response = self.client.get(url)
        # redirected to login page
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"/user/login/?next={url}")

        # registered user logged in but NOT project owner
        self.client.force_login(self.user2)

        # project owner logged in
        self.client.force_login(self.user1)
        # count no. projects before deletion
        project_count = Project.objects.count()

        response = self.client.get(url)
        # check that project was deleted
        self.assertEqual(Project.objects.count(), project_count - 1)
        self.assertNotEqual(Project.objects.first(), self.project1)
        self.assertEqual(Project.objects.first(), self.project2)

    def test_add_project_picture_get(self):
        template = "app_home/project_picture.html"
        url = reverse(
            "app_home:add-project-pic", kwargs={"pk": self.project1.pk}
        )

        # non logged in user
        response = self.client.get(url)
        # redirected to log in page
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"/user/login/?next={url}")

        # project owner logged in
        self.client.force_login(self.user1)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template)

    @mock.patch("cloudinary.uploader.upload")
    def test_add_project_picture_post(self, mock_uploader_upload):
        template = "app_home/project_picture.html"
        url = reverse(
            "app_home:add-project-pic", kwargs={"pk": self.project1.pk}
        )
        # number of pics before upload
        no_pics = len(self.project1.project_pic.all())

        # mocking
        mock_uploader_upload = "picture.jpg"

        # define URL & image
        mocked_picture = SimpleUploadedFile(
            "picture.jpg", b"file_content", content_type="image/jpeg"
        )
        # log project owner user in
        self.client.force_login(self.user1)
        # add the mocked picture to the project
        response = self.client.post(url, {"project_picture": mocked_picture})
        # redirected to project picture overview
        self.assertEqual(response.status_code, 302)
        # number of project pictures is increased by 1
        self.assertEqual(len(self.project1.project_pic.all()), no_pics + 1)

    # @mock.patch("cloudinary.uploader.upload")
    # def test_delete_project_picture_post(self, mock_uploader_upload):
    #     # logging in project owner
    #     self.client.force_login(self.user1)

    #     # setup - add a mocked picture
    #     template = "app_home/project_picture.html"
    #     url = reverse(
    #         "app_home:add-project-pic", kwargs={"pk": self.project1.pk}
    #     )

    #     # number of pics before upload
    #     no_pics = len(self.project1.project_pic.all())
    #     # mocking
    #     mock_uploader_upload = "picture.jpg"
    #     # define URL & image
    #     mocked_picture = SimpleUploadedFile(
    #         "picture.jpg", b"file_content", content_type="image/jpeg"
    #     )
    #     # add the mocked picture to the project
    #     response = self.client.post(url, {"project_picture": mocked_picture})

    #     # check that mocked picture is set
    #     self.assertEqual(len(self.project1.project_pic.all()), no_pics + 1)
    #     picture_object = self.project1.project_pic.get(project=self.project1.pk)

    #     # now delete the mocked picture
    #     template = "app_home/project_picture.html"
    #     url = reverse(
    #         "app_home:delete-project-pic", kwargs={"pk": picture_object.pk}
    #     )
    #     response = self.client.get(url)
    #     # test that the picture is deleted
    #     self.assertEqual(len(self.project1.project_pic.all()), no_pics)
