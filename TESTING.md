


CI
A continuous Integration (CI) file was added to the .github folder in order to perform automated testing in Github.
This CI file runs all unittests present in the project as well as black as a PEP8 compliance checker.


Unittests
Unittesting was used to test the main functionality of the site and confirm that all functions give the expected outputs. Unittests are automatically run on Github each time the code is pushed, using the CI file mentioned above.

UserView testing
Unittests were run for the following processes:
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


        print(response)
        # - user can log in with existing user
        response = self.client.post(
            self.url,
            data={
                "username": "user_created_for_testing",
                "password": "T35tP@55w0rd",
                "password2": "T35tP@55w0rd",
            },
        )
        
        self.assertNotEqual(first, second)

        # self.client.force_login(user=user)
        # - user receives feedback if login has failed
        # (e.g. incorrect password)

    def test_user_login_google(self):
        # - test user can sign up/in with google
        pass

    def test_user_login_github(self):
        # - test user can sign up/in with github
        pass







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