# Superclean Booking Service

* This is a project built using, Html, Css, Materializecss, Javascript, MongoDB, Flask and Python.

 The app contains a header elament which contains a
 * **Sign In** Button for users to sign into their accounts if they already have an account. 
 * **Register button** for users to create their accounts and a
 * **Sign Out buttons** that signs the users out from their accounts. 
 
 It also has a **Navigation Bar** that contains a Navigatation Menu such as **Home**, **Book A Clean**, and **Profile** page.
* The home displays all the bookings done by the different users,
* The **Book A Clean** provides a form for users to edit their cleanings and a 
* **Profile** page, that displays the users profile when they have created their accounts and are signed in.
* On the footer, is found a sub-title, social links and a **Sign out** button which is displayed only on small devices.

# UX
* The site is meant for users who want to book a cleaning or want to book the service from a cleaning company. The user can achieve the possibilities of creating, updating, deleting data from the database. The site provides the user with a menu that contains a **Book A Clean** option for the users to book their cleanings.
* As a user i can also delete informations by clicking on the delete button which will popup a message, asking the user to confirm the deleting process.
* As a user i can also update informations by clicking on the update button which will redirect the user to an updating form. On the form, the user can either cancel or continue with the update.
* If the users decide to update the information, it will flash a popup message, **"Booking Successfully Updated"** and redirects the user to the home page.

### Desktop view
<img src="static/images/wireframe2.jpg" width=600>

### Mobile view
<img src="static/images/wireframe1.jpg" width=200>

### ipad view
<img src="static/images/wireframe3.jpg" width=300>

# Features
In this section i will describe the different parts of the project.

## Existing Features
* The header contains the TITLE, SIGNIN, REGISTER AND LOGOUT
* The SignIn contains a signin form which has a **username** and **password** for users who have already created an account to sign into their accounts.
* The SignOut allows users to sign out of their accounts.
* The register contains a form that has a **username**, **password**, **confirm password** for users to create an account.
* The navigation bar contains a **Home**, **Book A Clean** and **Profile** menu.
* The **Home** page displays all the users bookings. And still on the home page, the user can **delete** or **update** informations they have created.
* The **delete** button when clicked asked the user to confirm the delete process.
* The **update** button redirects the user into an update form for the users to update the information. The update form has **cancel** and **update** buttons.
* The **cancel** button cancels the process and redirects the user back to the home page, while,
* The **update** button, confirms the users update.
* The **Book A Clean** provides a form for users to edit their booking. It has a **choose an option** for users to choose from the different cleanings. A **Task description** for users to describe elaborately what they want the company do for them. A **date** when they want their cleaning. An **address**, where to fill in their address, A **phone number** where to put their number and a **button** to click if the cleaning is urgent.
* Finally the **profile**, which shows the user's profile.

### Technology used
* **CSS, HTML, JS and PYTHON**
* **Materializecss** Is a framework used entirely to build the site. [Materializecss](https://materializecss.com/showcase.html).
* **MongoDB** Is the document-based datebase that can stores our data across multiple servers in the cloud [Link](https://www.mongodb.com/)
* **Flask** contains dependencies such werkzeug and jinga templating languages that python depends on to function properly. [Flask](https://flask.palletsprojects.com) 
### Library
* **flask-pymongo** is a third party library, that helps Flask to communicate with MongoDB and it is installed through **pip3 install flask-pymongo**
# Testing

## Users Testing
 The path through the website is Home, Book A Clean and profile.
### BOOK A CLEAN:
* Go to the "BOOK A CLEAN" page
* Try submitting an empty form, an error message appears on the required fields saying "please fill out the fields"
* Try filling the field with informations, the line turns green indicating the field has the required information.
* Try leaving the the field without filling the information, it turns red indicating no information present.
* try filling the fields with insufficient required information, it remains red.
* Try filling all the fields and submitting it popsup a message saying "Booking Successful" and redirects you to the home page.
### Home
* Go to the "HOME PAGE"
* Try clicking on the delete button, it popsup a message "Are you sure you want to delete this post" 
* Try clicking on the delete on the popup message, it deletes the message and flashes "Booking Successfully Deleted".
* Try clicking on the cancel button, it cancels and redirects you back to the home page.
* Try clicking on the update button it opens the form to be updated.
* Try clicking on the cancel button on the updated form, it brings you back to the home page.
* Try updating the form and click on the update button, it flashes a message "Booking Successfully Updated" and redirects you back to the home page.
* Try clicking the profile button which displays the users profile.
* Try clicking on the LOGOUT button, it logs the user out of his/her account and flashes a message "You have been logged out".
### On different screen Sizes
* On larger screens, the TITLE, SIGNIN, REGISTER and SIGNOUT buttons are displayed on the right, meanwhile, on the navigation menu, the HOME, BOOK A CLEAN and PROFILE are displayed to the right. The PROFILE is only displayed when the user is logged in.
* On smaller screens, the Title occupies the full width, meanwhile the SIGNOUT button is displayed on the Footer of the page. The Navigation menu icon is on the right and when clicked displays the menu from the right which contains the HOME, BOOK A CLEAN, PROFILE AND LOGOUT.

# Deployment
* The project was deployed to Heroku through the following stages.
* Firstly, I setup some files heroku needs to run my app, they are called dependencies such as requirments.txt and Procfile. 
* On the terminal, type **pip3 freeze > requirments.txt** this will create a requirements.txt file.
* On the terminal, type **echo web: python run.py > Procfile** this create the Procfile.
* Git **add**, **commit** and **push** the file to GitHub.
* Go to [Heroku website](https://dashboard.heroku.com/apps) and click on the button, **"NEW"**, it provides you with an option to "Creat new app", click on it.
* Fill in the **App Name** and your **region or region you are closest to**, then click on "Creat App" button.
* To connect the App, we can use **Automatic Deployment** from our GitHub repository by clicking on the **"GitHub Connect to Github"**, it displays your GitHub profile then add your repository name then click the "Search" button.
* When it finds your repo, click **connect**.
* Click on **"settings"** tap on your app and click on **"Reveal config vars"**. Fill in the config vars in the following ways.
      
               key    |     VALUE
      --------------- |----------------------------------------------------------------------------------------------------------------------
         DEBUG        |      FALSE 
         IP           |      0.0.0.0
         MONGO_URI    |      mongodb+srv://<username>:<password>@myfirstcluster.dgoye.mongodb.net/<database_name>?retryWrites=true&w=majority 
         PORT         |      5000   
         SECRET_KEY   |      <your_secret_key>
         MONGO_DBNAME |      <your_database_name> 
  
* Go back to your terminal and push your code to the master branch by using the following **steps**. **git status, git add -A, git commit -m "comments", finally git push**.
* Then, Go back to Heroku and "Enable Automatic Deploys" and then click "Deploy Branch" which will take a minute or two to build app.
* Once is done you will see, "your app was Successfully deployed".
* The deployed site is now available and will automatically update when ever we push changes to the GitHub repository.
* Here is a link to my deployed project on Heroku. [https://booking-times.herokuapp.com](https://booking-times.herokuapp.com)

## How to run this project locally
To clone this project into your gitpod, you will need to,
* Create a [Github Account](https://github.com/)
* use a chrome browser.
### Then follow these steps:

* Install the [Gitpod Browser Extension for chrome](https://chrome.google.com/webstore/detail/gitpod-dev-environments-i/dodmmooeoklaejobgleioelladacbeki).
* After installing restart the browser.
* Log into [Gitpod](https://gitpod.io/) with your gitpod account.
* Navigate to the [Project GitHub repository](https://github.com/gerardambe/bookings).
* Click on the **"green button"** in the top right corner of the repository.
* This will trigger a new gitpod workspace to be created from the code in github where you can work locally.

### To work on the project code within a local IDE such as VSCode or Pycharm
* Follow this link to the [Project GitHub repository](https://github.com/gerardambe/bookings)
* Next to the **green button**, click **clone** or **download**
* In the clone with HTTPs section,copy the clone URL for the repository.
* In your local IDE open the terminal.
* Change the current working directory to the location where you want the clone directory to be made.
* Type **git clone** and paste the URL you copied. e.g  
  **git clone https://github.com/gerardambe/bookings.git**
* press **enter** and your local clone will be created.


# CREDIT
* I owe a big thanks to all those who supported me in one way or another.
* Some ideas were obtained from materials at code institude.
* Meanwhile, some ideas where obtained from a video i watched on [utube](https://www.youtube.com/watch?v=u0oDDZrDz9U&t=2531s).

### Media
* The background photo was obtained from [Can Stock Photo](https://www.canstockphoto.com).

### Acknowledgements
* My inspiration came from a cleaning company website. When trying to understand how users where able to book and update and delete their cleanings.
