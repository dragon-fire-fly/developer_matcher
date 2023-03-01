Manual testing required:

- Responsiveness testing
- Browser compatibility testing
- Bugs resolved & unresolved
- Lighthouse testing outcomes
- Code validation
- User stories testing
- Features testing





CI
A continuous Integration (CI) file was added to the .github folder in order to perform automated testing in Github.
This CI file runs all unittests present in the project as well as black as a PEP8 compliance checker.


Unittests
Unittesting was used to test the main functionality of the site and confirm that all functions give the expected outputs. Unittests are automatically run on Github each time the code is pushed, using the CI file mentioned above.

UserView testing
Unittests were run for the following:
For app_user app:
1. Registration
    - Test that the user registration page successfully loads (status code 200) 
    - Test that the correct template is rendered for registration page
    - Test that form is submitted
    - Test that user is redirected (302 status) 
    - Test that redirection is to success page
    - Test that a new user is created in the db
    - Test that user is logged in and authenitcated following resistration
    - Test that a signup date is automatically generated
    - Test that no new user is created if form not valid
    - Test that browser redirects back to the form for resubmission if not valid

2. User login/logout
    - Test that the login page successfully loads (status code 200)  
    - Test that existing user is able to login
    - Test that existing user cannot log in with incorrect credentials
    - Test that user is redirected to home 

For app_home app:
views.py    
Home and about views
| Function Tested  | Function Type  | Status | Testing for.. | Assert Statement   |  Pass |
|---|---|---|---|---|---|
| Home view  | get  | not logged in  | correct template used| self.assertTemplateUsed(template)  | pass  |
|   |   |   | status code 200 (success) |  self.assertEqual(response.status_code, 200)  | pass  |
|   |   |   | Response contains... |  self.assertContains(response, "Please log in to continue")  | pass  |
|   |   | logged in user  | correct template used |  self.assertTemplateUsed(template)  | pass  |
|   |   |   | status code 200 (success) |  self.assertEqual(response.status_code, 200)  | pass  |
|   |   |   | Response doesn't contain... |  self.assertNotContains(response, "Please log in to continue")  | pass  |
| About view  | get  | any  | correct template used |  self.assertTemplateUsed(template)  | pass  |
|   |   |   | status code 200 (success) |  self.assertEqual(response.status_code, 200)  | pass  |

View other users
| Function Tested  | Function Type  | Status | Testing for.. | Assert Statement   |  Pass |
|---|---|---|---|---|---|
| Developer Overview page  | get  | not logged in  | correct template used |  self.assertTemplateUsed(template)  | pass  |
|   |   |   | status code 200 (success) |  self.assertEqual(response.status_code, 200)  | pass  |
|   |   |   | Response contains... |  self.assertContains(response, "Please log in or register to see other developers")  | pass  |
|   |   | logged in user  | correct template used |  self.assertTemplateUsed(template)  | pass  |
|   |   |   | status code 200 (success) |  self.assertEqual(response.status_code, 200)  | pass  |
|   |   |   | Response doesn't contain... |  self.assertNotContains(response, "Please log in or register to see other developers")  | pass  |
| Profile detail view (successful)  | get  | not logged in  | status code 302 (redirect) |  self.assertEqual(response.status_code, 302)  | pass  |
|   |   |   |  redirection url |  self.assertRedirects(response, f"/user/login/?next={url}")  | pass  |
|   |   | logged in user  | status code 200 (success) |  self.assertEqual(response.status_code, 200)  | pass  |
|   |   |   | correct template used |  self.assertTemplateUsed(response, template)  | pass  |
|   |   |   | check response contains user1 |  self.assertEqual(response.context["user"], self.user1)  | pass  |
|   |   |   | check response contains user2 |  self.assertEqual(response.context["user_for_profile"], self.user2)  | pass  |
| Profile detail view (profile does not exist)  | get  | logged in  | status code 404 (not found) |  self.assertEqual(response.status_code, 404)  | pass  |

View projects
| Function Tested  | Function Type  | Status | Testing for.. | Assert Statement   |  Pass |
|---|---|---|---|---|---|
| View project overview  | get  | not logged in  | correct template used |  self.assertTemplateUsed(template)  |   |
|   |   |   | status code 200 (success) |  self.assertEqual(response.status_code, 200)  |   |
|   |   |   | Response contains... |  self.assertContains(response, "Please log in or register to see projects")  | pass  |
|   |   | logged in user  | status code 200 (success) |  self.assertEqual(response.status_code, 200)  | pass  |
|   |   |   | correct template used |  self.assertTemplateUsed(response, template)  | pass  |
|   |   |   | Response contains... |  self.assertContains(response, self.project1.title)  | pass  |
|   |   |   | Response contains... |  self.assertContains(response, self.project2.title)  | pass  |
| View project overview (no projects)  | get  |   | status code 200 (success) |  self.assertEqual(response.status_code, 200)  | pass  |
|   |   |   | correct template used |  self.assertTemplateUsed(response, template)  | pass  |
|   |   |   | Response doesn't contain... |  self.assertNotContains(response, self.project1.title)  | pass  |
|   |   |   | Response doesn't contain... |  self.assertNotContains(response, self.project2.title)  | pass  |
| View project details  | get  | not logged in  | status code 302 (redirect) |  self.assertEqual(response.status_code, 302)  | pass  |
|   |   |   | redirection url |  self.assertRedirects(response, f"/user/login/?next={url}")  | pass  |
|   |   | user logged in  | status code 200 (success) |  self.assertEqual(response.status_code, 200)  | pass  |
|   |   |   | correct template used |  self.assertTemplateUsed(response, template)  | pass  |
|   |   |   | Response contains... |  self.assertContains(response, self.project1.title)  | pass  |
| View project details (project does not exist)  | get  | logged in user  | status code 404 (not found) |  self.assertEqual(response.status_code, 404)  | pass  |

Create a new project
| Function Tested  | Function Type  | Status | Testing for.. | Assert Statement   |  Pass |
|---|---|---|---|---|---|
| Create project  | get (get form)  | not logged in  | status code 302 (redirect) |  self.assertEqual(response.status_code, 302)  | pass  |
|   |   |   | redirection url |  self.assertRedirects(response, f"/user/login/?next={url}")  | pass  |
|   |   | logged in user  | status code 200 (success) |  self.assertEqual(response.status_code, 200)  | pass  |
|   |   |   | correct template used |  self.assertTemplateUsed(response, template)  | pass  |
| Create project  | post (valid)  | logged in user  | status code 302 (redirect) |  self.assertEqual(response.status_code, 302)  | pass  |
|   |   |   | project count increased by 1 |  self.assertEqual(Project.objects.count(), project_count + 1)  | pass  |
|   |   |   | new project title = "ProjectTitle3" |  self.assertEqual(Project.objects.last().title, "ProjectTitle3")  | pass  |
|   |   |   | new project contains lang 1 and 2|  self.assertCountEqual(Project.objects.last().p_language.all(),[self.language1, self.language2],)  | pass  |
|   |   |   | new project belongs to user 1|  self.assertEqual(Project.objects.last().user.last(), self.user1)  | pass  |
| Create project  | post (invalid)  | logged in user  | status code 302 (redirect) |  self.assertEqual(response.status_code, 302)  | pass  |
|   |   |   | project count has not increased |  self.assertEqual(Project.objects.count(), project_count)  | pass  |

Edit a project
| Function Tested  | Function Type  | Status | Testing for.. | Assert Statement   |  Pass |
|---|---|---|---|---|---|
| Edit project  | get (form) | not logged in  | status code 302 (redirect)  | self.assertEqual(response.status_code, 302)  | pass  |
|   |   |   | redirection url  | self.assertRedirects(response, f"/user/login/?next={url}")  | pass  |
|   |   | logged in (project owner)  | status code 200 (success)  | self.assertEqual(response.status_code, 200)  | pass  |
|   |   |   | correct template used  | self.assertTemplateUsed(response, template)  | pass  |
| Edit project  | post (valid)  | project owner  | status code 302 (redirect)  | self.assertEqual(response.status_code, 302)  | pass  |
|   |   |   | # projects has not changed  | self.assertEqual(Project.objects.count(), project_count)  | pass  |
|   |   |   | title is updated  | self.assertEqual(Project.objects.get(pk=self.project1.pk).title, "CHANGED TITLE!")  | pass  |
|   |   |   | description is updated  | self.assertEqual(Project.objects.get(pk=self.project1.pk).description,"CHANGED Project description3",)  | pass  |
|   |   |   | correct languages are saved  | self.assertCountEqual(Project.objects.get(pk=self.project1.pk).p_language.all(),[self.language1, self.language2],)  | pass  |
| Edit project  | post (invalid)  | project owner  | status code 200 (success)  | self.assertEqual(response.status_code, 200)  | pass  |
|   |   |   | correct template used  | self.assertTemplateUsed(response, template)  | pass  |
|   |   |   | # projects has not changed  | self.assertEqual(Project.objects.count(), project_count)  | pass  |
|   |   |   | title is unchanged  | self.assertEqual(Project.objects.get(pk=self.project2.pk).title, self.project2.title)  | pass  |
|   |   |   | description is unchanged  | self.assertEqual(Project.objects.get(pk=self.project2.pk).description,self.project2.description)  | pass  |
|   |   |   |  p langs are unchanged  | self.assertCountEqual(Project.objects.get(pk=self.project2.pk).p_language.all(),self.project2.p_language.all())  | pass  |

Delete a project
| Function Tested  | Function Type  | Status | Testing for.. | Assert Statement   |  Pass |
|---|---|---|---|---|---|
| Delete project  | get | not logged in   | status code 302 (redirect)  | self.assertEqual(response.status_code, 302)  | pass  |
|   |   |   | redirection url  | self.assertRedirects(response, f"/user/login/?next={url}")  | pass  |
|   |   | project owner  |  # projects has decreased by 1  | self.assertEqual(Project.objects.count(), project_count - 1)  | pass  |
|   |   |   | project 1 is no longer first in project list  | self.assertNotEqual(Project.objects.first(), self.project1)  | pass  |
|   |   |   | project 2 is now first in project list  | self.assertEqual(Project.objects.first(), self.project2)  | pass  |

Add project picture

| Function Tested | Function Type | Status | Testing for.. | Assert Statement | Pass |
|---|---|---|---|---|---|
| Add project picture  | get  | not logged in  | status code 302 (redirect)  | self.assertEqual(response.status_code, 302)  | pass  |
|   |   |   | redirection url  |  self.assertRedirects(response, f"/user/login/?next={url}") | pass  |
|   |   | project owner logged in  |   | self.assertEqual(response.status_code, 200)  | pass  |
|   |   | status code 200 (success)  | correct template used  | self.assertTemplateUsed(response, template)  | pass  |
|   | post (with mock)  | project owner  | status code 302 (redirect)  | self.assertEqual(response.status_code, 302)  | pass  |
|   |   |   | # pics increased by 1  | self.assertEqual(len(self.project1.project_pic.all()), no_pics + 1)  | pass  |

Delete project picture

| Function Tested | Function Type | Status | Testing for.. | Assert Statement | Pass |
|---|---|---|---|---|---|
| Delete project pic  | get  | project owner  | ensure that mocked picture has been added first  | self.assertEqual(len(self.project1.project_pic.all()), no_pics + 1)  | pass  |
|   |   |   | mocked picture has been deleted  | self.assertEqual(len(self.project1.project_pic.all()), no_pics)  | pass  |
|   |   |   |   |   | pass  |
|   |   |   |   |   | pass  |

1. function tested assert statement type pass?



Manual Testing
To be tested when project completed:

User registration and log in:
- User registration page loads correctly
- login page loads correctly
- User can submit form on registration page
- new user is successfully created
- feedback if account creation failure
- user logged in and redirected correctly to home page after signing up
- user can sign up with google
- user can sign up with github
- user can log in with existing user
- user receives feedback if login has failed (e.g. incorrect password)


Authentication and security
- only logged in users can view developer page
- only logged in users can view project page
- users can see that they are logged in
- only validated users can edit their own profile page
- only validated users can delete their own profile page
- sensitive user details (e.g. email address) is not displayed to other users


User Profile
- user can edit profile details
- user can delete their profile
- user can add profile pictures
- user can delete profile pictures

Developer page overview
- developer overview page renders correctly and shows all users except logged in user
- clicking on a developer will take the user to that developers profile page


Project page overview
- project overview page renders correctly and shows all projects
- clicking on a project will take the user to that project detail view page