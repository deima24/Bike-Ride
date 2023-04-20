# Bike-Ride

BikeRide is a activity sharing site for anyone that has a good story to tell about there experince or an idea. It provides users a clear and simple way to browse and share ideas on things to keep kids entertained.


# User-Experience-Design

## Site Goals

The site is aimed at anyone that has an interesting story to tell about there expericen or an idea. Without signing in the user can browse ideas and see other people storyes. They will also be able to log on and share ideas of their own and comment on other people’s posts. They will also be able to edit and delete their ideas.

## Agile Planning

![agile](media/images/agile.png)

This project was developed using agile methodologies. All the features had to be done to make this web so user could use it. All the features were added from a agile. 


# Scope

Home page with information about BikeRide.
Restricted features for not logged in users.


## Structure

Navbar
user story - As a user I want to be able to navigate easily around the site easily from any devise

Navigation Menu
When the user is not logged in the navigation menu links to the Home page, Ride Blog page, Register and the Login in page

![navbarnolog](media/images/nav%20bar%20not%20loged%20in.png)

Once the user has signed in the navigation menu changes to Home, Ride Blog, Create a post and Logout

The user will also receive a message saying they have successfully signed in.

![logedIn](media/images/Loged%20In.png)

on smaller devices, the menu options collapse into a button

![smallernavbar](media/images/nav%20smaller%20size.png)

## Home page

User Story - As a user I want the front page to be clear and self-explanatory so I know I am in the right place

The front page contains a main image of the bike on the road. This will make it evident to the user that the website is about the bike rides.

![mainpageimg](media/images/main%20img.png)

Under this image is information about the site and how to share and browse rides.

![mainpagetext](media/images/mainpgtext.png)


## Footer

User Story: As site owner, I want to share social media links and contact details

The Footer has been added to the bottom of the site and contains links to social media sites so that users can also share their ideas and promote the site via social media.

![pagefooter](media/images/footer.png)


## RideBlog

User Story: As a user that is not logged in, I want to be able to browse ideas from other users.

Anybody can use the website to browse post, they are shown in the Ride Blog page with the titles and pictures in rows of 3 and 6 posts per page. The post Title is a link to open up each post with further information about it. Also You can read the beginning of the post.

![post](media/images/posts.png)


## Post Details

User Story: As a user, I want to be able to comment and like otherpeople’s ideas

Each user story opens up to a full page which contains the image, a full content of the post and read post comments.

![contentpostandcomment](media/images/contentandcomments.png)

Logged-on users can also comment on and like the ideas.

![comment](media/images/comment.png)

![likes](media/images/like.png)


## Sign in, log in, log out

As a new user, you are able to sign up easily.
As a returning user, you are able to log in easily.
As a user, you are able to log out of the site safely and easily.
As a developer, I want to ensure the forms are all the same style and look good on all devices.

Users can sign in and out using forms and confirmation pages. These forms were made using allauth and edited using bootstrap.

![SignIn](media/images/SignIn.png)

![SignUp](media/images/SignUp.png)

![SignOut](media/images/SignOut.png)
