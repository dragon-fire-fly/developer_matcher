# Developer Connect

## Repository
The live site can be found at [developer-connect.herokuapp.com](https://developer-connect.herokuapp.com/).

## Objective
The objective of Developer Connect is to link software developers up with eachother so that they can form teams and work on projects. Furthermore, a project posting board allows the opportunity for people with app, website or software ideas to build a team with the appropriate skills and technological experience to bring their idea(s) to life. The platform also provides a way for developers to connect with one another and for potential employers to find their next ideal candidate.

### Am I Responsive mockup 
TODO: add mockup image at following path:
![screenshot](documentation/mockup.png)


## UX

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

In this section, you will briefly explain your design processes.


🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

### Colour Scheme
The ["minty"](https://bootswatch.com/minty/) bootswatch theme was utilised for this project as it provides a simple, clean design with an appealing green colour as its base. The buttons have soft, rounded edges which are visually appealing and the colours used for primary, secondary, warning and danger buttons complement eachother nicely. Many "card" elements and modals were used in this project, and Minty's card and modal styles are simple, aesthetically pleasing and do not distract from the content of the website.

Following assessment with an [EightShapes](https://contrast-grid.eightshapes.com/?version=1.1.0&background-colors=&foreground-colors=%23FFFFFF%2C%20White%0D%0A%23000%0D%0A%235A5A5A%0D%0A%2378C2AD%0D%0A%23F3969A%0D%0A%23C63D17%0D%0A%23FFCE67%0D%0A&es-color-form__tile-size=compact&es-color-form__show-contrast=aaa&es-color-form__show-contrast=aa&es-color-form__show-contrast=aa18&es-color-form__show-contrast=dnp) contrast grid, some of the Minty colours were deemed to not have sufficient contrast for visually impaired users. In particular, many of the areas where white text was used were replaced with black text to improve readability. More details about this can be found in the  [TESTING.md](TESTING.md) file.

Adaptations to the "minty" theme:
- `#FFFFFF` used for nav bar and most button text -> changed in most cases to `#000000`
- `#FF7851`, an orange for 'danger' buttons -> changed to `#C63D17`, a darker red, for better contrast with white text
- `#5a5a5a` a medium gray -> changed in areas with small font text or on coloured backgrounds (nav bar, buttons) to `#000000`

The general colour scheme can be seen below:
![Developer Connect colour scheme](documentation/design/colour-scheme.png)

The [coolers colour scheme](https://coolors.co/78c2ad-f3969a-c63d17-ffce67-5a5a5a) shown above shows the basic colours used for the site.

<!-- ⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

If you've used CSS `:root` variables, consider also including a code snippet here!

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

I've used CSS `:root` variables to easily update the global colour scheme by changing only one value, instead of everywhere in the CSS file.

```css
:root {
    /* P = Primary | S = Secondary */
    --p-text: #000000;
    --p-highlight: #E84610;
    --s-text: #4A4A4F;
    --s-highlight: #009FE3;
    --white: #FFFFFF;
    --black: #000000;
}
``` -->

### Typography

The fonts contained within the "minty" Bootswatch theme were used for this project.
Additional icons from the [Font Awesome](https://fontawesome.com) library were used. Icons were used throughout the site, including the social media icons in the footer and the edit/delete icons for messages. The icons used are shown below:

![FontAwesome icons](documentation/design/fa-icons.png)

## User Stories

User stories are an integral part of software design and execution and help not only with the design on the features but also with the management of the project. User stories represent the small units of work which can be undertaken during an iteration (or "sprint"). 

In this project, User Stories are broken down from three "Epics". Epics are large overarching concepts which define the major parts of the software being developed. These epics were then dissected into smaller User Stories. The epics used for this project were:
1. Account Management  
2. User interaction  
3. Project interaction

Github actions was used to record epics and user stories and a [User Story template](https://github.com/dragon-fire-fly/developer_matcher/blob/main/.github/ISSUE_TEMPLATE/user-story.md) was created and used for the purpose of recording the user stories and for breaking them down into "acceptance criteria" - the conditions which must be met in order for the User Story to be considered "finished" - and "tasks" - the actual work that needs to be done in order to meet these acceptance criteria.

The User Stories are listed below and are linked to the respective issue on Github actions:


| Issue #  | Epic  | User Story  | Prioritisation  | Implemented   |
|---|---|---|---|---|
| 1  | Account Management  |  [As a **new site user** I can **create a new user account** so that **I can log into and use the full functionality of the site**](https://github.com/dragon-fire-fly/developer_connect/issues/1)  | Must-do  | Yes  |
| 2  | Account Management  | [As a **registered user** I can **log in to my user account** so that **I can access full functionality of the site**](https://github.com/dragon-fire-fly/developer_connect/issues/2)   |  Must-do | Yes  |
| 3  | Account Management  | [As a **registered user** I can **view, update and delete my profile** so that **I can amend and delete my data**](https://github.com/dragon-fire-fly/developer_connect/issues/3)  | Must-do  |  Yes |
| 5  |  User interaction   | [As a **registered user** I can **see an overview of other users on the site** so that **I can get an overview of the skills, interests and projects of other users**](https://github.com/dragon-fire-fly/developer_connect/issues/5)  | Must-do  | Yes  |
| 6  | User interaction  | [As a **registered user** I can **view the profiles of other users** so that **I can see whether this user is interesting to me based on my interests, programming languages, current projects, etc.**](https://github.com/dragon-fire-fly/developer_connect/issues/6)  | Must-do  | Yes  |
| 8  | Project interaction  | [As a **registered user** I can **see an overview of all the active projects posted on the site** so that **I can read details about the projects and decide which are potentially of interest to me**](https://github.com/dragon-fire-fly/developer_connect/issues/8)  | Must-do  | Yes  |
| 9  |  Project interaction | [As a **registered site user** I can **view the details of active projects** so that **I can assess if the project is of interest to me, if my skills and experience are suitable for the project and contact the project owner**](https://github.com/dragon-fire-fly/developer_connect/issues/9)  | Must-do  | Yes  |
| 39  | Project Interaction  | [As a **registered user** I can **create a new project** so that **I can advertise the project to other, potentially interested users**](https://github.com/dragon-fire-fly/developer_matcher/issues/39)  | Must-do  | Yes  |
| 40  | Project Interaction  | [As a **project owner** I can **edit and delete my own projects** so that **I can update the details or remove the project from the site**](https://github.com/dragon-fire-fly/developer_matcher/issues/40)  | Must-do  | Yes  |
| 42  | Project Interaction  | [As a **project owner** I can **add and remove images for my project** so that **other users can get a visual idea of the project**](https://github.com/dragon-fire-fly/developer_matcher/issues/42)  | Must-do  | Yes  |
| 4  | Account Management  |  [As a **google account holder** I can **log in with my Gmail account** so that **I do not have to manually enter my details or create a password when signing up to the site**](https://github.com/dragon-fire-fly/developer_connect/issues/4)  | Should-do  | Yes  |
| 59  |  User Interaction | [As a **logged in user** I can **see a maximum number of entries per page and navigate through pages** so that **the page loading time is not too long and I do not get overwhelmed with too many entries**](https://github.com/dragon-fire-fly/developer_matcher/issues/59) | Should-do  | Yes  |
| 68  | User Interaction  | [As the **sender of a message** I can **edit my message** so that **I can change its contents** and as both a **sender and receiver of a message** I can **delete a message** so that I can **remove it from my account**](https://github.com/dragon-fire-fly/developer_matcher/issues/68)  | Should-do  | Yes  |
| 10  |  User interaction | [As a **registered site user** I can **like and message other users** so that **I can interact with other users and discuss interests or projects**](https://github.com/dragon-fire-fly/developer_connect/issues/10)  | Could-do  | Partially  |
| 7  | User interaction    | [As a **registered site user** I can **perform a search for other users based on a variety of parameters** so that **I can more easily find the type of user I am looking for**](https://github.com/dragon-fire-fly/developer_connect/issues/7)  | Could-do  | Partially  |
| 12  | Project interaction  | [As a **registered site user** I can **perform a search for projects based on a variety of parameters** so that **I can more easily find the type of project I am looking for**](https://github.com/dragon-fire-fly/developer_connect/issues/12)  | Could-do  | Partially  |
| 11  | Project interaction  | [As a **registered site user** I can **star and add comments to projects** so that **I can interact with projects, share my ideas and contact the project owner**](https://github.com/dragon-fire-fly/developer_connect/issues/11)  | Could-do  | No  |


## Wireframes

To follow best practice and to help with planning, wireframes were developed for mobile, tablet, and desktop sizes.
[Balsamiq](https://balsamiq.com/wireframes) was used to design the site wireframes. The table below shows the wireframes in all three sizes (mobile, tablet and desktop).

### Home Page Wireframes

| Page | Wireframes (mobile, tablet, desktop) |
| --- | --- |
| Log in page | ![screenshot](documentation/wireframes/home_login.png) |
| Registration page | ![screenshot](documentation/wireframes/register.png) |
| Individual Profile page | ![screenshot](documentation/wireframes/profile.png) |
| About page | ![screenshot](documentation/wireframes/about.png) |
| Find Developer Page | ![screenshot](documentation/wireframes/find_developers.png) |
| Find Projects page | ![screenshot](documentation/wireframes/find_projects.png) |

## Features

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

In this section, you should go over the different parts of your project,
and describe each in a sentence or so.

You will need to explain what value each of the features provides for the user,
focusing on who this website is for, what it is that they want to achieve,
and how your project is the best way to help them achieve these things.

For some/all of your features, you may choose to reference the specific project files that implement them.

IMPORTANT: Remember to always include a screenshot of each individual feature!

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

### Existing Features

- **Navbar**

    - The navbar makes navigation around the site easy and intuitive for the user. On the left hand side, the 'Developer Connect' logo is displayed and links back to the home page. The other three links bring the user to the Developer Overview, Project Overview and About pages. On the right hand side, if the user is not yet logged in, they are invited to do so with 'sign in' and 'sign up' links and a message saying "Get connected now!".
    If the user is already registered and logged in, 
Navbar (user not logged in)
![Navbar](documentation/features/navbar-not-logged-in.png)
Navbar(user logged in)
![Navbar](documentation/features/navbar-logged-in.png)

- **Homepage**

    - The homepage displays the "Developer Connect" logo and either "sign in" and "sign up" buttons, if no user is logged in, or hello ((username)) if a user is logged in

![Hompage](documentation//features/home-page.png)

- **Registration page**

    - The registration page allows new users to register to the site. A form is provided which asks for desired username, e-mail address and a password, repeated twice. The constraints for password choice are displayed on the registration page. Users are informed if their chosen username is unavailable or unacceptable (see validation below).

![Registration page](documentation/features/register-page.png)

- **Login page**

    - The login page allows users who have registered on the site previously to log in with their credentials. There is also the option for a google or github log in.

![Login page](documentation/features/sign-in-page.png)


- **Developer Overview Page**

    - The Developer Overview page displays all the users registered on the site, excluding the currently logged in user. 8 users are displayed per page (see pagination below for more details)

![Developer Overview Page](documentation/features/developer-overview-page.png)


- **Project Overview Page**

    - The Project Overview page displays all the projects made by users on the site (including any created by the logged in user). 4 projects are displayed per page (see pagination below for more details)

![Project Overview Page](documentation/features/project-overview-page.png)

- **User Profile Page (logged in user)**

    - The User Profile page shows the profile for the currently logged in user and may be accessed through the dropdown menu on the right hand side of the nav bar (under the user's picture). The profile page shows all detaila of the user, including their e-mail address. 
    The user's primary profile picture is displayed in the centre of the screen and when clicked, navigates the user to the "add profile picture" page. If the user does not yet have a profile picture, a placeholder picture will be displayed, with text explaining that this is a placeholder piture and may be changed by clicking the photo and uploading a picture.
    This placeholder picture is a randomly generated photo of a kitten, from [Place Kitten](https://placekitten.com/).

![User Profile Page](documentation/features/profile_page.png)
![Placeholder picture](documentation/features/kitten-placeholder.png)

- **Edit User Profile Page(logged in user)**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/features/edit-profile-page.png)

- **Feature**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/features)

- **Feature**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/features)


- **Feature**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/features)


- **Feature**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/features)



⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

Repeat as necessary for as many features as your site contains.

Hint: the more, the merrier!

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

### Future Features

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

Do you have additional ideas that you'd like to include on your project in the future?
Fantastic! List them here!
It's always great to have plans for future improvements!
Consider adding any helpful links or notes to help remind you in the future, if you revisit the project in a couple years.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- Cool new feature #1
    - Any additional notes about this feature.
- Cool new feature #2
    - Any additional notes about this feature.
- Cool new feature #3
    - Any additional notes about this feature.

## Tools & Technologies Used

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

In this section, you should explain the various tools and technologies used to develop the project.
Make sure to put a link (where applicable) to the source, and explain what each was used for.
Some examples have been provided, but this is just a sample only, your project might've used others.
Feel free to delete any unused items below as necessary.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- [HTML](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [CSS](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [CSS :root variables](https://www.w3schools.com/css/css3_variables.asp) used for reusable styles throughout the site.
- [CSS Flexbox](https://www.w3schools.com/css/css3_flexbox.asp) and/or [CSS Grid](https://www.w3schools.com/css/css_grid.asp) used for an enhanced responsive layout.
- [Bootstrap](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [Materialize](https://materializecss.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [JavaScript](https://www.javascript.com) used for user interaction on the site.
- [Python](https://www.python.org) used as the back-end programming language.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [GitHub Pages](https://pages.github.com) used for hosting the deployed front-end site.
- [Gitpod](https://gitpod.io) used as a cloud-based IDE for development.
- [Markdown Builder by Tim Nelson](https://traveltimn.github.io/markdown-builder) used to help generate the Markdown files.
- [Flask](https://flask.palletsprojects.com) used as the Python framework for the site.
- [Django](https://www.djangoproject.com) used as the Python framework for the site.
- [MongoDB](https://www.mongodb.com) used as the non-relational database management with Flask.
- [SQLAlchemy](https://www.sqlalchemy.org) used as the relational database management with Flask.
- [PostgreSQL](https://www.postgresql.org) used as the relational database management.
- [ElephantSQL](https://www.elephantsql.com) used as the Postgres database.
- [Heroku](https://www.heroku.com) used for hosting the deployed back-end site.
- [Cloudinary](https://cloudinary.com) used for online static file storage.
- [Stripe](https://stripe.com) used for online secure payments of ecommerce products/services.
- [AWS S3](https://aws.amazon.com/s3) used for online static file storage.

## Database Design

Entity Relationship Diagrams (ERD) help to visualize database architecture before creating models.
Understanding the relationships between different tables can save time later in the project.

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

Using your defined models (one example below), create an ERD with the relationships identified.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

```python
class Product(models.Model):
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
```

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

A couple recommendations for building free ERDs:
- [Draw.io](https://draw.io)
- [Lucidchart](https://www.lucidchart.com/pages/ER-diagram-symbols-and-meaning)

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

![screenshot](documentation/erd.png)

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

Using Markdown formatting to represent an example ERD table using the Product model above:

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- Table: **Product**

    | **PK** | **id** (unique) | Type | Notes |
    | --- | --- | --- | --- |
    | **FK** | category | ForeignKey | FK to **Category** model |
    | | sku | CharField | |
    | | name | CharField | |
    | | description | TextField | |
    | | has_sizes | BooleanField | |
    | | price | DecimalField | |
    | | rating | DecimalField | |
    | | image_url | URLField | |
    | | image | ImageField | |

## Agile Development Process

### GitHub Projects

[GitHub Projects](https://github.com/dragon-fire-fly/developer_matcher/projects) served as an Agile tool for this project.
It isn't a specialized tool, but with the right tags and project creation/issue assignments, it can be made to work.

Through it, user stories, issues, and milestone tasks were planned, then tracked on a weekly basis using the basic Kanban board.

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

Consider adding a basic screenshot of your Projects Board.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

![screenshot](documentation/gh-projects.png)

### GitHub Issues

[GitHub Issues](https://github.com/dragon-fire-fly/developer_matcher/issues) served as an another Agile tool.
There, I used my own **User Story Template** to manage user stories.

It also helped with milestone iterations on a weekly basis.

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

Consider adding a screenshot of your Open and Closed Issues.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- [Open Issues](https://github.com/dragon-fire-fly/developer_matcher/issues)

    ![screenshot](documentation/gh-issues-open.png)

- [Closed Issues](https://github.com/dragon-fire-fly/developer_matcher/issues?q=is%3Aissue+is%3Aclosed)

    ![screenshot](documentation/gh-issues-closed.png)

### MoSCoW Prioritization

I've decomposed my Epics into stories prior to prioritizing and implementing them.
Using this approach, I was able to apply the MoSCow prioritization and labels to my user stories within the Issues tab.

- **Must Have**: guaranteed to be delivered (*max 60% of stories*)
- **Should Have**: adds significant value, but not vital (*the rest ~20% of stories*)
- **Could Have**: has small impact if left out (*20% of stories*)
- **Won't Have**: not a priority for this iteration

## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

**IMPORTANT:**
- ⚠️ DO NOT update the environment variables to your own! These should NOT be included in this file; just demo values! ⚠️
- ⚠️ DO NOT update the environment variables to your own! These should NOT be included in this file; just demo values! ⚠️
- ⚠️ DO NOT update the environment variables to your own! These should NOT be included in this file; just demo values! ⚠️

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

The live deployed application can be found deployed on [Heroku](https://developer-connect.herokuapp.com).

### ElephantSQL Database

This project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:
- Click **Create New Instance** to start a new database.
- Provide a name (this is commonly the name of the project: developer_matcher).
- Select the **Tiny Turtle (Free)** plan.
- You can leave the **Tags** blank.
- Select the **Region** and **Data Center** closest to you.
- Once created, click on the new database name, where you can view the database URL and Password.

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.
- For *Primary interest*, you can choose *Programmable Media for image and video API*.
- Optional: *edit your assigned cloud name to something more memorable*.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | user's own value |
| `DATABASE_URL` | user's own value |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | user's own value |

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:
- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:
- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:
- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:
- Select **Automatic Deployment** from the Heroku app.

Or:
- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.
- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("CLOUDINARY_URL", "user's own value")
os.environ.setdefault("DATABASE_URL", "user's own value")
os.environ.setdefault("SECRET_KEY", "user's own value")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:
- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/dragon-fire-fly/developer_matcher) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/dragon-fire-fly/developer_matcher.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/dragon-fire-fly/developer_matcher)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/dragon-fire-fly/developer_matcher)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

Use this space to discuss any differences between the local version you've developed, and the live deployment site on Heroku.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

## Credits

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

In this section you need to reference where you got your content, media, and extra help from.
It is common practice to use code from other repositories and tutorials,
however, it is important to be very specific about these sources to avoid plagiarism.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

### Content

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

Use this space to provide attribution links to any borrowed code snippets, elements, or resources.
A few examples have been provided below to give you some ideas.

Ideally, you should provide an actual link to every resource used, not just a generic link to the main site!

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

| Source | Location | Notes |
| --- | --- | --- |
| [Markdown Builder by Tim Nelson](https://traveltimn.github.io/markdown-builder) | README and TESTING | tool to help generate the Markdown files |
| [Chris Beams](https://chris.beams.io/posts/git-commit) | version control | "How to Write a Git Commit Message" |
| [W3Schools](https://www.w3schools.com/howto/howto_js_topnav_responsive.asp) | entire site | responsive HTML/CSS/JS navbar |
| [W3Schools](https://www.w3schools.com/howto/howto_css_modals.asp) | contact page | interactive pop-up (modal) |
| [W3Schools](https://www.w3schools.com/css/css3_variables.asp) | entire site | how to use CSS :root variables |
| [Flexbox Froggy](https://flexboxfroggy.com/) | entire site | modern responsive layouts |
| [Grid Garden](https://cssgridgarden.com) | entire site | modern responsive layouts |
| [StackOverflow](https://stackoverflow.com/a/2450976) | quiz page | Fisher-Yates/Knuth shuffle in JS |
| [YouTube](https://www.youtube.com/watch?v=YL1F4dCUlLc) | leaderboard | using `localStorage()` in JS for high scores |
| [YouTube](https://www.youtube.com/watch?v=u51Zjlnui4Y) | PP3 terminal | tutorial for adding color to the Python terminal |
| [strftime](https://strftime.org) | CRUD functionality | helpful tool to format date/time from string |
| [WhiteNoise](http://whitenoise.evans.io) | entire site | hosting static files on Heroku temporarily |

### Media

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

Use this space to provide attribution links to any images, videos, or audio files borrowed from online.
A few examples have been provided below to give you some ideas.

If you're the owner (or a close acquaintance) of all media files, then make sure to specify this.
Let the assessors know that you have explicit rights to use the media files within your project.

Ideally, you should provide an actual link to every media file used, not just a generic link to the main site!
The list below is by no means exhaustive. Within the Code Institute Slack community, you can find more "free media" links
by sending yourself the following command: `!freemedia`.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

| Source | Location | Type | Notes |
| --- | --- | --- | --- |
| [Pexels](https://www.pexels.com) | entire site | image | favicon on all pages |
| [Lorem Picsum](https://picsum.photos) | home page | image | hero image background |
| [Unsplash](https://unsplash.com) | product page | image | sample of fake products |
| [Pixabay](https://pixabay.com) | gallery page | image | group of photos for gallery |
| [Wallhere](https://wallhere.com) | footer | image | background wallpaper image in the footer |
| [This Person Does Not Exist](https://thispersondoesnotexist.com) | testimonials | image | headshots of fake testimonial images |
| [Audio Micro](https://www.audiomicro.com/free-sound-effects) | game page | audio | free audio files to generate the game sounds |
| [Videvo](https://www.videvo.net/) | home page | video | background video on the hero section |
| [TinyPNG](https://tinypng.com) | entire site | image | tool for image compression |

### Acknowledgements

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

Use this space to provide attribution to any supports that helped, encouraged, or supported you throughout the development stages of this project.
A few examples have been provided below to give you some ideas.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- I would like to thank my Code Institute mentor, [John/Jane Doe](https://github.com/username) for their support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) tutor team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support; it kept me going during periods of self doubt and imposter syndrome.
- I would like to thank my spouse/partner (John/Jane), for believing in me, and allowing me to make this transition into software development.
- I would like to thank my employer, for supporting me in my career development change towards becoming a software developer.
