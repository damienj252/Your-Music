#Single Webpage Application
##Created by Damien Joyce
####Data Representation and Querying Project 2016

This repository contains code for one of my Third year Software Development projects. The module is Data Representation and Querying. 

###Project Overview
I have created a Single-Page Web Application that allows the user store the name of their favorite artists and songs and store them on a database using sqlite.

###My Project outline are as follows:
>You are required to develop a single-page web application(SPA) written in the programming language Python using the Flask framework. You must devise an idea for a web application, write the software, write documentation explaining how the application works, and write a short user guide for it.

In the beginning of this project I found it very difficult to create a webpage that can extend to another webpage that I created but I could not rectify this error so because of this I created a single webpage application with no extensions.

###Attempts
I made many different attempts to create the desired webpage. My first attempt was to create a webpage that could access two other webpages I created.The main page was to give information to the user of how this webpage worked. The second webpage should have allowed the user add their favorite artists and songs and output them to the third webpage while saving them on a database. The third page was suppose to output all the information added in by the user but after accessing the other two pages the browser was unable to find the page. I then decided to stop and start again by creating a single webpage that gave the user the same access as the three combined.

###References
I have used the Jquery, Thetehr, bootstrap and  ajax.googleleap to edit the appearance of the webpage application. I have used SQlite as a database to store the data entered into the database called music.db stored in the data folder. I used the html and javascript code that I have learned in previous modules while attending GMIT Galway.All other refrences are noted on the top of each page saying original source.


###What would I change about my project
I would have tried to keep it simple from the beginning by using just a single webpage application instead of a multiple webpage application which gave me much difficulty in trying to get working. If I could have accessed the database I would have the search bar working also but I did not organise my time correctly and eventually ran out of time trying to rectify these errors. I would also have the information of all the data entered to output to the index.html file if I had organised my time better.


###How to run the application.
After flask is install the user must go to the desired folder where the project is stored using terminal or CMDR. To run the application the user must have python 3.5.2 (Latest verson of anaconda 4.2.0) installed on their device. Then they must run these commands:
```bash
$ python setup.py
$ python app.py
```

Using the URL provided by the terminal input it into a browser and the webpage will appear.