# Developer Connect

## Repository
The live site can be found at [developer-connect.herokuapp.com](https://developer-connect.herokuapp.com/).

## Objective
The objective of Developer Connect is to link software developers up with eachother so that they can form teams and work on projects. Furthermore, a project posting board allows the opportunity for people with app, website or software ideas to build a team with the appropriate skills and technological experience to bring their idea(s) to life. The platform also provides a way for developers to connect with one another and for potential employers to find their next ideal candidate.

### Am I Responsive mockup 
![Am-i-responsive mockup](documentation/am_i_responsive_mockup/amiresponsive.png)

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

![Epics](documentation/github_issues/github-epics.png)

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


More information about the Agile process can be found in the [Agile Development Process](#agile-development-process) section.

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
    Users may also register using their Google or Github account.

![Registration page](documentation/features/register-page.png)
Social registration:  
![Social sign ons](documentation/features/social_signins.png)

- **Login page**  

    - The login page allows users who have registered on the site previously to log in with their credentials. There is also the option for a google or github log in.

![Login page](documentation/features/sign-in-page.png)
Social sign in:  
![Social sign ons](documentation/features/social_signins.png)


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

![User Profile Page](documentation/features/profile-page.png)
![Placeholder picture](documentation/features/kitten-placeholder.png)

- **Edit User Profile Page(logged in user)**  

    - Users can edit their profile by clicking "Edit" on their profile page. Only the logged in user may edit their profile. The user is taken to an edit form which is pre-filled with their existing data. If the user clicks "update", the data is updated, the user receives a notification message and they are redirected back to their profile page.

![Edit profile page](documentation/features/edit-profile-page.png)

- **Delete User Account**  

    - Users are able to delete their own account by clicking "delete" on their user profile. Only the logged in user may delete their account. Before account deletion occurs, the user is prompted with a confirmation modal to ensure they really want to delete their account and haven't clicked delete by mistake.

![Delete user account](documentation/features/delete-user-profile.png)

- **Profile Picture Overview**  

    - When the user clicks on the picture on their User account (see 3 features up), they are taken the the profile picture overview page. From here they may upload new profile pictures or delete existing ones. The first uploaded picture becomes the profile picture displayed on their public profile and the thumbnail picture in the nav bar. Pictures are uploaded to [Cloudinary](https://cloudinary.com/) where they are stored and retreived and upon deletion, they are also deleted from Cloudinary.

![Profile Picture Overview page](documentation/features/profile-pic-overview.png)


- **Profile Picture CRUD**  

    - User profile pictures have partial "CRUD" functionality. A user can create (upload) a new image, read (view) an uploaded picture and delete a picture. The create-view-delete cycle is shown below. When deleting a profile picture, the user is prompted to confirm that they really want to delete the chosen picture with a pop-up modal to prevent accidental deletion. Messages are shown when upload and deletion functions successfully complete.

![CRUD functions for profile pictures](documentation/features/crud-profile-pic.png)


- **Other User Profile**  
    User profiles for users other than the logged in user may be viewed by the logged in user. Most of the details are the same as on the logged in user's own profile, but the e-mail address is omitted for privacy. The logged in user cannot edit or delete another user's account, nor add/remove photos from another user's profile, but they can send a message to the other user through their profile page by clicking the "Send message" button.
![Individual profile of another user](documentation/features/individual-profile.png)


- **Project CRUD**  

    - Projects have full "CRUD" functionality. A user can create (upload) a new project, read (view) an existing project, edit their own projects and delete their own projects. The create-view-edit-delete cycle is shown below.
    In the create phase, the user completes a project creation form stating the title and programming languages required for the project. They may also optionally include a project description. If successfully created, the user receives a success message and is redirected to the detail page for the newly created project.
    As shown in the "project read" section, the project now appears on the project overview page for all logged in users, has an individual project page with the details and is listed under "projects" for the user that created it.
    The project may be updated only by the user that created it (or an admin in the admin panel) and all of the fields may be edited.
    The project may be deleted at any time by the user that created it (or an admin in the admin panel). Before deletion, the user receives a pop-up modal to confirm they want to delete their project. If "Delete my project" is selected, the user receives a "project successfully deleted message at the top of the screen. When a project is deleted, all associated pictures are also deleted (including from Cloudinary).
    If a user is deleted, the project remains on the project page but no longer has a user associated with it.

![CRUD functionality of projects](documentation/features/crud-project.png)

- The buttons available vary depending on who owns the project. If the logged in user is the project owner, they can edit and delete the project, as well as adding or changing the photo (by clicking on it). If the logged in user does not own the project, they will have the option to message the project owner directly, or to visit the project owner's profile by clicking their name. They cannot edit or delete the project.

![Different project views](documentation/features/project-views.png)

- **Create New Project**  

    - The create new project form is shown here on multiple screen sizes to demonstrate the responsiveness of the project creation form. Users can select at least one programming language (relabeled from "P language" to "Programming language(s)" since these screenshots were taken)

![Create new project form](documentation/features/create-project.png)

- **Project Picture CRUD**  

    - Project pictures have partial "CRUD" functionality. A user can create (upload) a new image, read (view) an uploaded picture and delete a picture. The create-view-delete cycle is shown below. When deleting a project picture, the user is prompted to confirm that they really want to delete the chosen picture with a pop-up modal to prevent accidental deletion. Messages are shown when upload and deletion functions successfully complete.

![CRUD functionality for project pictures](documentation/features/crud-project-pic.png)

- **Messages Inbox and Sent Messages**  

    - Each registered user has a messages inbox and a sent messages mail box. These can be accessed by hovering over the user's profile picture in the navigation bar and selecting "My messages". This brings the user to the received messages "inbox" page. To access the "outbox", the user clicks the "Sent messages" button at the top. Inversely, to get back to the inbox from the sent messages page, the user clicks the "Received messages" button, or accesses again through the navigation bar.

    The layout of the message lists varies depending on the screen size of the device used. For smaller devices, only the key information is displayed - username of the sender/recevier, title of the message and the sent/received date and time. If users use a device with a screen width of 768px or above, they can also see a thumbnail of the sender/receiver's profile picture and they have the option to delete (and edit, if the sender) from this list view. If using a screen size of below 768px, users must go into the individual message if they wish to edit or delete the message.
    Users of all screen sizes may access the user profile of the sender/receiver by clicking their username and may access the individual message by clicking the message title.

![Message inbox](documentation/features/message-inbox.png)
![Message outbox](documentation/features/messages-sent.png)

- **Messages CRUD**  

    - The messaging feature has full "CRUD" functionality. Users can create new messages, view both sent and received messages, edit messages they sent and delete messages they sent or received. 
    Once edited, the message displays a small "edited" text at the end of the message. Only the sender may edit a particular message, but either party may delete a message. In this case, the message is deleted from the database and is no longer visible to either the sender or the receiver.

![CRUD functionality of messages](documentation/features/crud-messages.png)

- **Send new message**  

    - The send new message form is fully responsive and shows the profile picture of the message receiver as well as their username. 

![Send new message form](documentation/features/send-new-msg.png)
- The new message form can be accessed from three locations. 
    1. The user profile of the selected user
    2. The project page - the project owner can be messaged directly from here
    3. If a message has been received from another user, this user may be messaged back by clicking "Reply".

    Pressing cancel will take the user to the message inbox, regardless of which page the user came from.
![Options for sending a message](documentation/features/send-msg-options.png)

- **Edit message**  

    - Once a message has been sent, it may be edited by the user who sent it. Only the sender may edit the message. Once edited, a small "edited" will appear at the end of the message to indicate that changes were made from the original message. Pressing cancel will take the user back to the message. Pressing edit message will take the user back to their inbox and will display a "Message successfully updated" message.
    If using a screen size of 768px or above, users may edit messages directly from the sent messages list. Otherwise, users from all screen sizes may edit messages from the individual message page.

![Edit message form](documentation/features/edit-msg.png)

- **Delete message**  

    - Messages may be deleted by either the sender or the receiver. If one party deletes the message, it will be deleted from the database and will therefore no longer be accessible for either party. Before deletion occurs, the user is prompted with a pop-up modal to confirm if they really want to delete the message. It also warns that the message will be deleted for both the sender and the receiver.
    If using a screen size of 768px or above, users may delete messages directly from the inbox or sent messages list. Otherwise, users from all screen sizes may delete messages from the individual message page.

![Delete message and modal](documentation/features/delete-msg.png)

- **Individual messages**  

    - From the inbox/ sent messages page, individual messages may be accessed by clicking on the title. The contents of this individual page varies slightly depending on whether it is a sent or received message. In both cases, an image of the user is displayed at the top with eiter the text "Your message to ((username))" or "Message from ((username))". Both message types then display the title and message with the option to go back to messages, view the user's profile or delete the message. If it is a sent message, the option to "Edit message" is present. If it is a received message, the option to "Reply" is present.

Individual sent message page
![Individual sent message page](documentation/features/individual-msg-sent.png)
Individual received message page
![Individual received message page](documentation/features/individual-msg-received.png)

- **Django Messages**  

    - The Django messages feature is utilised in this project to provide feedback to the user. The messages are displayed at the top of the screen for all screen sizes, just under the navigation bar. The messages are styled with bootstrap.
![Django messages](documentation/features/django-messages.png)
The following image shows screenshots of the messages in action. All CRUD functions give user feedback via these messages.
![Types of django messages](documentation/features/django-messages-types.png)

- **Filtering**  

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![The filtering panels](documentation/features/filter-panels.png)

![An example of filtering](documentation/features/filter-example.png)

- **Pagination**  

    - Django's Paginator class is utilised to provide pagination for the Developer Overview, Project Overview and messages pages. Both of these pages have a navigation panel at the bottom of the screen showing how many pages are available, the current page (highlighed in pink) and previous and next buttons. Users can nagivate using the previous and next buttons as long as a previous or next page is available (for example, the "previous" button will not work if the user is on page 1). If one or both of these buttons are unavailable, they will be greyed out as shown below and be will become non-clickable.

![Pagination feature](documentation/features/pagination.png)

Pagination works alone but can also be combined with the filtering mentioned above. The site is set up to recieve arguments in the url for filtering, pagination, or both. The screenshot below demonstrates some of the different combinations possible.
The base url for the developer page is `https://developer-connect.herokuapp.com/developers/` and queries can be made using `.../developers/?` followed by the query. This can be either `p_language=(num)` or `page=(num)`.

![The urls for filtered and/or paginated pages](documentation/features/urls-filter-paginate.png)



### Future Features  

There are many features which could be added to the project at a later date but were not deemed important for this iteration of the project implementation. Some ideas for future features include:

- A notification system for messages
    - This would allow users to see when they have recevied a new message instead of having to manually check their inbox. This would be extremely helpful for the overall user experience of the site and is the highest priority future feature.

- The ability to add other users to the project 
    - This would mean that all the users associated with a particular project would be listed under the project and not just the project owner. This would help with networking and getting involved in projects more easily.

- The ability to favourite users and projects to be able to quickly find them again in the future
    - Having a "Favourites" page for projects and users would streamline the site, particularly if there became a large number of users on the site. If there are 100+ users, for example, it may be difficult to find a particular user just by browsing through pages or past messages.

- Search and sort functionality for Developer and Project Overview pages and messages
    - Similar to the "favourites" page above, having search and sort functionality would help with finding specific users or re-finding a user you were interested in before. This would be an extension of the "filtering" feature currently implemented in the project.

- Addition of other skills users could select in addition to programming languages - such as frameworks, dadabases and stacks.
    - This would help find specific users or projects more easily if, for example, a project requires Django expertise with postgreSQL, or any other combination of frameworks, databases, etc.

- A password reset function
    - This would help returning users if they have forgotten their password or wish to reset it for any reason (e.g. a data breach on another site)

- Email notification system for sign up, unauthorised accessed, password reset, new message etc.
    - This would help improve the user experience by providing extra security and adding a professional touch. It could also improve engagement with the site, for example receiving an email when they receive a message or having a reminder email after a period of inactivity.

- An administrator area where administrators can have an overview of users, projects etc. and make amendments without needing to go into the admin panel
    - This could streamline the administration of the site and improve the user experience for administrator users.

## Tools & Technologies Used

- [HTML](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [CSS](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
<!-- - [CSS :root variables](https://www.w3schools.com/css/css3_variables.asp) used for reusable styles throughout the site. -->
- [CSS Flexbox](https://www.w3schools.com/css/css3_flexbox.asp)
- [Bootstrap](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [Bootswatch](https://bootswatch.com/) used as an extension to Bootstrap to provide pleasant aesthetics for the site.
- [Python](https://www.python.org) used as the back-end programming language.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [Gitpod](https://gitpod.io) used as a cloud-based IDE for development.
- [Markdown Builder by Tim Nelson](https://traveltimn.github.io/markdown-builder) used to help generate the Markdown files.
- [Django](https://www.djangoproject.com) used as the Python framework for the site.
- [PostgreSQL](https://www.postgresql.org) used as the relational database management.
- [ElephantSQL](https://www.elephantsql.com) used as the Postgres database.
- [Heroku](https://www.heroku.com) used for hosting the deployed back-end site.
- [Cloudinary](https://cloudinary.com) used for online static file storage.
- [Visual Studio Code](https://code.visualstudio.com/) used as a local IDE for development.
- [Black](https://pypi.org/project/black/) used as a PEP8 compliant Python code formatter
- [DBeaver](https://dbeaver.io/) used to produce ERDs and help plan the database models
- [Balsamiq](https://balsamiq.com/) used to produce wireframes

## Database Design
An Entity Relationship Diagram (ERD) was created using [DBeaver](https://dbeaver.io/) in order to visualize the database architecture before creating Django models.

The ERD is shown below. There are 6 models which interact with eachother in a relational manner. 
The six models are:

1. User
2. User profile picture
3. Project
4. Project profile picture
5. Programming language
6. Messages

The relationships are either one-to-many or many-to-many in nature, as discussed below.

![Entity relationship diagram](documentation/design/ERD.png)

The following models have a one-to-many relationship:
- One user can have many profile pictures but each profile picture only has one user
- One project can have many pictures but each picture only has one project
- One user can write (or receive) many messages but each message only has one sender and one receiver.

The remaining relationships are many to many:
- One user can have many programming languages and each programming language can have many users associated with it
- One project can have many programming languages and each programming language can have many projects associated with it
- One user can have many projects and each project can (theoretically) have many users associated with it*

These three models form a "square" on the ERD as they require intermediate tables to store the many-to-many relationship details. On the ERD these intermediate tables are labelled as "user-project", "project-p-language" and ""user-to-p-language" and they store the id of the two relevant tables. For example, in the "user-to-p-language" table, the id of a user1 could be associated with programming languages 1 and 2, but at the same time programming language 1 could be associated with many other users. This table provides an interface between the user table and the programming language table so that these relationships may be stored and related information may be accessed from both ends.

*This backwards relationship has not yet been implemented, but it is on the list of future features that each project may have many users associated with it.

An example of a model used in the project is shown below:

```python
class Project(models.Model):
    user = models.ManyToManyField(User, blank=True)
    p_language = models.ManyToManyField("ProgramLang")
    title = models.CharField(
        help_text="What is the title for your project?",
        max_length=100,
        unique=True,
    )
    description = models.TextField(
        help_text="Enter your project description here", blank=True, null=True
    )

    def __str__(self):
        return f"<Project name: {self.title}>"

    def delete(self, *args, **kwargs):
        """
        Additional function to ensure pictures are deleted
        from cloudinary
        """
        # delete associated profile pics
        for pic in self.project_pic.all():
            pic.delete()
        # then delete itself
        super().delete(*args, **kwargs)
```

This `Project` model inherits from Django's inbuilt `Model` class and utilises two many-to-many relationships. One between itself and the `User` class (which may be blank, incase an associated user account is deleted), and one between itself and the `ProgramLang` class (which may not be blank). The model then has a `title` CharField with a maximum length of 100 characters (limited as this is displayed on a bootstrap card) which must be unique. An optional `description` TextField may be as long as a user desires and may be left blank.

The `__str__` method returns `<Project name: ((project title))>` so that the project may be easily identified in the admin panel.

A `delete` method extends the default delete method to call the delete method for each picture associated with the project, which in turn deletes the pictures from Cloudinary (this Cloudinary delete method can be seen at `app_user/models.py` lines 137-144).

This `Project` model is represented as a table below as an example:

| **id** (unique) | Type | Notes |
| --- | --- | --- |
| user | ManyToManyField | MTM to **User** model |
| p_language | ManyToManyField | MTM to **ProgramLang** model |
| title | CharField | Max length 100 chars |
| description | TextField | |


## Agile Development Process

### GitHub Projects

[GitHub Projects](https://github.com/dragon-fire-fly/developer_matcher/projects) served as an Agile tool for this project.
It isn't a specialized tool, but with the right tags and project creation/issue assignments, it can be made to work.

Through it, user stories, issues, and milestone tasks were planned, then tracked on a weekly basis using the basic Kanban board. An overview of the Kanban board is shown below. Newly created issues began in the "Backlog" column and were moved through the "Ready to Begin", "In Progress" and "Testing" columns before being maked as closed and moved to the "Done" column.

![GitHub Project Board](documentation/github_issues/github-project-board.png)

### GitHub Issues

[GitHub Issues](https://github.com/dragon-fire-fly/developer_matcher/issues) served as an another Agile tool.

There, I used my own **User Story Template** to manage user stories and **Bug Report Template** to report bugs as they were discovered.
For each User Story, at least three **Acceptance Criteria** were recorded to indicate the criteria that must be fulfilled in order for the User story to be completed and at least three **Tasks** which must be performed in order to fulfil said criteria.
![User Story Template](documentation/github_issues/user-story-template.png)

The Bug Report Template is based off the Bug report template provided by Github with some minor modifications to add the tag "bug" and automatically assign it to a user.
![Bug Report Template](documentation/github_issues/bug-report-template.png)


Below, the open and closed issues can be seen. These helped with milestone iterations on a weekly basis. The list below includes all issues including **User Stories** and **Bugs**.

- [Open Issues](https://github.com/dragon-fire-fly/developer_matcher/issues)

    ![Open issues screenshot](documentation/github_issues/open-issues.png)

- [Closed Issues](https://github.com/dragon-fire-fly/developer_matcher/issues?q=is%3Aissue+is%3Aclosed)

    ![Closed Issues Screenshot](documentation/github_issues/closed-issues.png)
    ![Closed Issues Screenshot page 2](documentation/github_issues/closed-issues-2.png)

### MoSCoW Prioritization

I've decomposed my Epics into stories prior to prioritizing and implementing them.
Using this approach, I was able to apply the MoSCow prioritization and labels to my user stories within the Issues tab.

- **Must Have**: guaranteed to be delivered (*max 60% of stories*)
- **Should Have**: adds significant value, but not vital (*the rest ~20% of stories*)
- **Could Have**: has small impact if left out (*20% of stories*)
- **Won't Have**: not a priority for this iteration

These labels were added to the default ones provided by Github and can be seen in the screenshot below:
![Github Labels](documentation/github_issues/github-labels.png)

### Branches

Branches were utilised within GitHub to help seperate areas of focus and to enable more information to be given about a series of commits and how they relate to the GitHub issues mentioned earlier. This was extremely valuable for managing which user story (or other task, such as testing or documentation) was being focused on at the time and helped keep the workflow organised. 

Branching may be performed in in Visual Studio Code or GitPod using the following CLI commands:

| CLI command | Notes |
| --- | --- |
| `git branch` | list current branches |
| `git checkout <branchname>` | switch to specified branch |
| `git checkout -b <branchname>` | create new branch (if it doesn't exist) and switch to it |
| `git branch -d <branchname>` | delete specified branch |
| `git push origin <branchname>` | pushes the specified branch to GitHub |


### Pull requests 

Once ready to merge from the created branch back to the main branch, a pull request may be made on GitHub.

Below are some screenshots of the pull request and merging process:   
![Pull request and merge](documentation/github_issues/github-merge-process.png)

Normally, a reviewer would be assigned to check the pull request before merging it to the main branch, however I was the only one working on this project and therefore this was not possible.

[Pull requests](https://github.com/dragon-fire-fly/developer_matcher/pulls) from different branches are accessed here.
![Closed pull requests](documentation/github_issues/github-prs-1.png)
![Open pull requests](documentation/github_issues/github-prs-2.png)


Below is an example pull request. Pull requests contain the details of the commits contained within them and in most cases they have been linked to the issues and milestones that they relate to with a description.

![Example pull request](documentation/github_issues/example-pr.png)


## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file. This includes User Story testing.

## Deployment

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


## Credits
### Content

| Source | Location | Notes |
| --- | --- | --- |
| [Markdown Builder by Tim Nelson](https://traveltimn.github.io/markdown-builder) | README and TESTING | tool to help generate the Markdown files |
| [Pylessions user registration](https://pylessons.com/user-registration) | models and forms | user registration |
| [Generic views](https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-editing/) | views | generic views |
| [Uploading Images](https://docs.djangoproject.com/en/4.1/topics/http/file-uploads/) | image upload (projects and profile forms) | uploading images in django |
| [Profanity checking](https://pypi.org/project/better-profanity/) | user and project creation and edit forms | profanity checking |
| [LoginRequiredMixin](https://docs.djangoproject.com/en/4.1/topics/auth/default/) | entire site | authentication of user |
| [Bootstrap Pagination](https://getbootstrap.com/docs/5.0/components/pagination) | templates and views | Pagination for Django |
| [Codemy Pagination Youtube](https://www.youtube.com/watch?v=wY_BNsxCEi4) | templates and views | Pagination for Django|
| [Django unittesting](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing) | entire site | unittesting for Django |
| [Learn Django AllAuth](https://learndjango.com/tutorials/django-allauth-tutorial) | entire site | authentication with AllAuth |
| [Pylessons AllAuth](https://pylessons.com/django-google-oauth) | entire site | authentication with AllAuth |
| [Crispy Forms](https://simpleisbetterthancomplex.com/tutorial/2018/08/13/how-to-use-bootstrap-4-forms-with-django.html) | forms, templates | improving form styling with crispy forms |
| [Cloudinary image upload API](https://cloudinary.com/documentation/image_upload_api_reference) | image uploads | uploading images throught the cloudinary API |
| [Bootstrap Navbar](https://getbootstrap.com/docs/5.0/components/modal/) | entire site | implementing bootstrap navbar |
| [Bootstrap Cards](https://getbootstrap.com/docs/4.0/components/card/#card-columns) | templates | displaying cards in developer and project overview pages |
| [Horizontal bootstrap cards](https://www.tutlane.com/example/bootstrap/bootstrap-horizontal-card-example) | templates | making project overview cards display horizontally |
| [Logo creation](https://www.shopify.com/tools/logo-maker/) | entire site, home page | creation of a logo and favicon for the site |
| [Cat sample images](https://beta.dreamstudio.ai/dream) | developer profiles | AI for creating unique images for samples user profiles |
| [WhiteNoise](http://whitenoise.evans.io) | entire site | hosting static files on Heroku temporarily |

### Media
| Source | Location | Type | Notes |
| --- | --- | --- | --- |
| [404 image](https://www.freepik.com/free-vector/two-people-connecting-plug-socket-man-woman-pulling-cords-with-outlet-plug-flat-illustration_12291325.htm#query=cartoon%20connected%20plug&position=2&from_view=search&track=robertav1)| entire site | image | 404 page image |
| [500 image](https://www.freepik.com/free-vector/tiny-people-examining-operating-system-error-warning-web-page-isolated-flat-illustration_11235921.htm#&position=49&from_view=author) | entire site | image | 500 page image |
| [Coffee image](https://www.pexels.com/photo/close-up-photography-of-cup-of-coffee-851555/) | project page | image | image for online coffee shop sample project |
| [No img/ upload img](https://pixabay.com) | project page | image | placeholder image for projects without a user uploaded image |
| [Gallery image](https://www.pexels.com/photo/abstract-wallpaper-2860804/) | project page | image | image for online gallery sample project  |
| [Poker image](https://www.pexels.com/photo/a-person-holding-gaming-cards-6664195/) | project page | image | image for online poker sample project |
| [Face detection image](https://pixabay.com/illustrations/face-detection-scan-to-scan-4760281/) | project page | image | image for face detection sample project |
| [Cat sample images](https://beta.dreamstudio.ai/dream) | developer page | image | Most of the images for the sample user accounts were created using dreamstudio |

### Acknowledgements

- I would like to thank my Code Institute mentor, [Tim Nelson](https://github.com/TravelTimN) for his support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) tutor team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support; it kept me going during periods of self doubt and imposter syndrome, particularly the class of May 2022.
- I would also like to thank Peer Hoffmann for his help with unittesting, testing the application using Safari and for his general support and friendship. It is very appreciated!
- I would like to thank my husband (Christian Schmidt), for believing in me, and allowing me to make this transition into software development.
