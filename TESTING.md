


CI
A continuous Integration (CI) file was added to the .github folder in order to perform automated testing in Github.
This CI file runs all unittests present in the project as well as black as a PEP8 compliance checker.


Unittests
Unittesting was used to test the main functionality of the site and confirm that all functions give the expected outputs. Unittests are automatically run on Github each time the code is pushed, using the CI file mentioned above.

UserView testing
Unittests were run for the following processes:
1. Registration
- Test that the user registration page successfully loads (status code 200) the correct 
    - Test that a new use can successfully register on the site









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