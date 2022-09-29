<h1 align="center">MK || CookBook</h1>

[MK || Cookbook]( https://cookbook-mk-ms3-project.herokuapp.com/)

This is my 3rd Project for Code Institute, which futures python. Unfortunately I did not have the time to complete the website as I wanted I will
write down what will the upcoming futures be

<h2 align="center"><img src="static\assets\ms3_validation_tests\Untitled.png" alt="screenshot taken from AmIresponsivesite showing the webpages responsiveness on a Laptop , Desktop and Mobile"></h2>

## Table of contents
1. [User Experience (UX)](#user-experience-ux)
    + User Stories
    + Design
    + Wireframes
2. [Features](#features) 
    + Existing Features
    + Upcoming Features
3. [Technologies Used](#technologies-used)
    + Languages Used
    + Frameworks, Libraries & Progragms Used
4. [Testing](#testing)
5. [Deployment on Github](#deployment-on-github)
6. [Deployment on Heroku](#deployment-on-heroku)
7. [Credits](#credits)

## User Experience (UX)

+ ### User Stories

    + First Time Visitors

      For first time Visitors my aim is have the recipes shown in the main screen, and the about tab to be visible.
      Also for the Login/Register Buttons to be available.

    + Returing Visitors

      Returning visitors should be able to quickly log in and taken straight to their favorite page and also to be able to add their own recipes.
      In the future I want to user to be able to re-edit their own recipes and update them as required.
+ ### Design

  + Colour Scheme

     + I picked a theme from [Free Boostrap Themes](https://startbootstrap.com/) as I didnt have the time on this project to create the site all by myself
  
  + Imagery 
     
     + The photos I used were links from [Fine Dining Lovers](https://www.finedininglovers.com/), I just used copy image address to test that the recipes have images. 
     In the future I want to add jpeg/png images taken by me and also users
     to be able to add their own jpeg images(this will be subject to review before posting)

+ ### Wireframes

    + I didnt use wireframes for this project

## Features

+ Responsive on all device sizes
+ Vanilla JavaScript
+ Interactive Elements 
+ Animation done in CSS3
+ A cook book work in progress.

## Upcoming Features 

+ Users will be able to search recipes in their favorites tab and search bar will be animated
+ Autocomplete and search accuracy will be improved
+ Users will be able to choose whether the recipe they add will be public or private
+ Template cards for recipes will be re-designed to be more interactive.
+ Will add CSS and JS into Add-recipe form which I didnt have the time to do now.

## Technologies Used 

### Languages Used
+ [HTML 5](https://en.wikipedia.org/wiki/HTML5)
+ [CSS3](https://en.wikipedia.org/wiki/CSS)
+ [JAVASCRIPT](https://en.wikipedia.org/wiki/JavaScript)
+ [PYTHON 3.X](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used
1. [Font Awesome](https://fontawesome.com)
    + Font Awesome used for social Icons
2. [Git](https://git-scm.com)
    + Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
3. [Github](https://github.com)
    + GitHub is used to store the projects code after being pushed from Git.
4. [FLASK FRAMEWORK](https://en.wikipedia.org/wiki/Flask_(web_framework))
5. [MONGO DB](https://en.wikipedia.org/wiki/MongoDB)

## Testing

+ [JSHint](https://jshint.com/)
+ [W3C Markup Validator](https://validator.w3.org/#validate_by_uri+with_options)
+ [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
+ [PEP8](http://pep8online.com/) - This website has now expired as ( 29.09.2022 ) I have used Pylint


### Testing User Stories
+ First Time Visitors
  
  For first time Visitors my aim is have the recipes shown in the main screen, and the about tab to be visible.
  Also for the Login/Register Buttons to be available. This is now achieved and when a first time visitor comes to the site can see
  all the recipes. The login/Register buttons are visible and in differnt color to attract the eye.

  First time visitor are able to understand the content off the site from the first page.

  First time visitor can not see the favorite tab unless the register.

+ Returing Visitors
  
  Returning visitors should be able to quickly log in and taken straight to their favorite page and also to be able to add their own recipes.
  This was achieved, the re-turning visitors once they have logged in they get re-directed on their favourites page.

  Returning visitors can navigate quickly on the main page and view all recipes.

+ Frequent Visitors (chefs, cooks etc)

  Frequent visitors might find usefull to read the about page. 

  About page can be seen. In the future this will be like a blog page, which I want to encourage futured Chefs to showcase their work and recipes encouraging
  visitors to try cooking at home.
  

### Further Testing
+ The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge, Opera and Safari browsers.
+ The website was viewed on a variety of devices such as Desktop, Laptop, Samsung S22 Ultra and iPhoneX.
+ A large amount of testing was done to ensure that all pages were linking correctly. 
+ I personally have access in 27" 2K Monitor, a 17" Laptop, Android phone which I constatly used for testing.
+ I have used Chrome Developer Tools as Opera Dev Tools to constantly check the website responsivness.
+ Fixed issue with responsiveness on small devices and added better user experience on recipes on index.html and favorites.html
+ As I dont want more images on the markdown please find the testing screenshots on the ms3_validation_tests folder. This can be achieved if you navigate on my github page then go to COOKBOOK-PROJECT repository there you will find a folder named static then navigate to assets folder which you can see a subfolder ms3_validation_tests folder. If you right click on that folder you will see the images I have uploaded.
Alternatively you can click [here](https://github.com/Frangelicomk/cookbook-project/tree/main/static/assets/ms3_validation_tests) to see the folder on my github straight away.

### Difficulties Encountered & Bugs
+ Known Bug: The user can add and remove from favorites on the recipe screen, while the user can see 
the recipes favorited on the favorites tab when pressing view more and un-favorite button on that page the app crashes.
I dont know how to fix this yet. - This has now been fixed 17.05.2022 by adding an if statement to check which page the user is on.
+ Known Bug: While I have added two fields for passwords when someone registers I couldnt make the validations for these 2 fields.
so if the user adds a password and then adds different password on repeat-password field user will still be registered with the first entry.
Also there is no message appearing yet when the username is taken. The page will be just refreshed. - Flash messages now display as they should be
and verifications works.
+ Some URLs for images dont show as it should be. The plan in the future is to let the users add images, subject to review by admins.
+ I found it difficult creating some of the def in python and then make them work on each page. It was difficult to add blocks of code using flask.
I believe this will come with practice.


## Deployment on Github 

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://github.com) in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.

```
## Deployment on Heroku

### Heroku

The project was deployed to Heroku following the next steps:
1. Create a requirements.txt file using the terminal command `pip3 freeze > requirements.txt`.
2. Create a Procfile with the terminal command `echo web: python app.py > Procfile`.
3. Proceed with git add and git commit the new requirements and Procfile and then git push the project to GitHub.
4. Create a new app on [Heroku website](https://dashboard.heroku.com/) by clicking the "New" button on your dashboard. Give it a name and set the region to Europe.
5. From the Heroku dashboard of your newly created application, click on "Deploy", "Deployment method" and "select Github".
6. Confirm the linking of the Heroku app to the correct Github repository.
7. In the Heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".
8. Set the following config vars:
IP : 
MONGO_URI : 
PORT : 
SECRET_KEY : 
9. Click on enable deployment.
10. Wait until you get notified a the bottom of the page that your app is deployed and vie the deployment.

## Credits

### Code
+ All code was written by Michael Kefalas
+ Authentication for users log in/register and log out was copied from Flask Mini Project from Code Institute videos.

### Content 
+ All content was written by Developer and Designer Michael Kefalas

### Acknowledgements 
+ Youtubers which i got inspired from :
  + [Kevin Powell](https://www.kevinpowell.co) for his amazing videos regarding CSS and Grid , his approach on designs is something I want to learn and also I am having his
  course as well for Flexbox
  + [Gary Simon](https://dribbble.com/Coursetro) has been a great inspiration and you can follow his discord channel [here!](https://discord.gg/wQQtgNey)
+ [Mozila Developer](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API) for the awesome explaination of the canvas future. Everything you need for Javascript can be found 
  there as well.
+ [George Karabassis](https://www.fiverr.com/gorgeka111) a big thanks to the most amazing Tutor/Mentor out there.
+ Also I have to thank [Nescafe](https://www.nescafe.com/gb/) which is my go to go Coffee helping me maintain my eyes open while coding late in the evening.This doesnt count as
an ad right? And if i continue like this I will Acknowledge Specsavers as they will soon provide me with glasses :)