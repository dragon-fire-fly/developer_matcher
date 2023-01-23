
# Developer Matcher

## Repository
<!-- Link to repo here once live -->

## Objective
The objective of Developer Matcher (better name pending...) is to link software developers up with eachother so that they can form teams and work on projects. Furthermore, a project posting board allows the opportunity for people with app, website or software ideas to build a team with the appropriate skills and technological experience to bring their idea(s) to life. The platform also provides a way for developers to connect with one another and for potential employers to find their next ideal candidate.


## User Experience
### User Stories
1. [As a **new site user** I can **create a new user account** so that **I can log into and use the full functionality of the site**](https://github.com/dragon-fire-fly/developer_matcher/issues/1)(issue #1)
2. [As a **registered user** I can **log in to my user account** so that **I can access full functionality of the site**](https://github.com/dragon-fire-fly/developer_matcher/issues/2)(issue #2)
3. [As a **registered user** I can **view, update and delete my profile** so that **I can amend and delete my data**](https://github.com/dragon-fire-fly/developer_matcher/issues/3)(issue #3)
4. [As a **google account holder** I can **log in with my Gmail account** so that **I do not have to manually enter my details or create a password when signing up to the site**](https://github.com/dragon-fire-fly/developer_matcher/issues/4)(issue #4)
5. [As a **registered user** I can **see an overview of other users on the site** so that **I can get an overview of the skills, interests and projects of other users**](https://github.com/dragon-fire-fly/developer_matcher/issues/5)(issue #5)
6. [As a **registered user** I can **view the profiles of other users** so that **I can see whether this user is interesting to me based on my interests, programming languages, current projects, etc.**](https://github.com/dragon-fire-fly/developer_matcher/issues/6)(issue #6)
7. [As a **registered site user** I can **perform a search for other users based on a variety of parameters** so that **I can more easily find the type of user I am looking for**](https://github.com/dragon-fire-fly/developer_matcher/issues/7)(issue #7)
8. [As a **registered user** I can **see an overview of all the active projects posted on the site** so that **I can read details about the projects and decide which are potentially of interest to me**](https://github.com/dragon-fire-fly/developer_matcher/issues/8)(issue #8)
9. [As a **registered site user** I can **view the details of active projects** so that **I can assess if the project is of interest to me, if my skills and experience are suitable for the project and contact the project owner**](https://github.com/dragon-fire-fly/developer_matcher/issues/9)(issue #9)
10. [As a **registered site user** I can **like and message other users** so that **I can interact with other users and discuss interests or projects**](https://github.com/dragon-fire-fly/developer_matcher/issues/10)(issue #10)
11. [As a **registered site user** I can **star and add comments to projects** so that **I can interact with projects, share my ideas and contact the project owner**](https://github.com/dragon-fire-fly/developer_matcher/issues/11)(issue #11)
12. [As a **registered site user** I can **perform a search for projects based on a variety of parameters** so that **I can more easily find the type of project I am looking for**](https://github.com/dragon-fire-fly/developer_matcher/issues/12)(issue #12)

### WireFrames
Initial wireframe ideas:

![Log in page](documentation/wireframes/home_login.png)
![Register](documentation/wireframes/register.png)
![Profile page](documentation/wireframes/profile.png)
![About page](documentation/wireframes/about.png)
![Find developers page](documentation/wireframes/find_developers.png)
![Find projects page](documentation/wireframes/find_projects.png)


## Features



### Future Features

## Technologies Used
1. HTML, CSS, Python/Django Framework



## Testing

## Bugs

### Resolved Bugs

### Remaining Bugs

## Deployment
### Github

### Heroku
- Create new app on Heroku

- Create django secret key with https://djecrety.ir/
- Add secret key to Heroku config variables
- Add DATABASE_URL to Heroku config variables 
- disable collectstatic with `heroku config:set DISABLE_COLLECTSTATIC=1`

- Create a Procfile and add `web: gunicorn developer_matcher.wsgi:application` to allow gunicorn to act as the web server
- Add Heroku app to list of allowed hosts in settings.py `ALLOWED_HOSTS = ['locahost', '127.0.0.1', 'developer-matcher.herokuapp.com']`

## Credits

Cloudinary:
https://cloudinary.com/documentation/image_upload_api_reference

CSS/bootstrap:
navbar:
https://getbootstrap.com/docs/4.0/components/navbar/
cards:
https://getbootstrap.com/docs/4.0/components/card/#card-columns

Crispy forms:
https://simpleisbetterthancomplex.com/tutorial/2018/08/13/how-to-use-bootstrap-4-forms-with-django.html

