Milestone Project 3

# Let's Hike

This website is my third project after the culmination of studying Practial Python and Data Centric Development, including Flask and the MongoDB database system.

The website can be found at [Let's Hike](https://ms3-hikingtrails.herokuapp.com/home)

## UX

This website was developed for users who have an interest in hiking within the United Kingdom and the Republic of Ireland. They will be greeted on the home page with a landing page picture with a simple title stating the purpose of the website. For more information on the purpose and benefit of the website users can visit the about page.
Users will be able to implement the CRUD system in order to create, review, update and delete hikes with useful data presented for other hikers to visit those sites. 

## User stories:

As a user on a mobile/tablet or desktop device I would:

* Want to have a clear idea of the website purpose after visiting the home page
* Want to click the About button in the navbar and visit the About page
* Want to click the Hikes button in the navbar and visit the Hikes page
* Want the Hikes page to have all existing Hikes displayed in a clear format
* Want to click the Add Hikes button in the navbar and visit the Add Hikes page
* Want to be able to fill out a clear form on the Add Hikes page to add my data to the website
* Want to be able to edit an existing hike by clicking the edit button
* Want to be able to edit data on the Edit Hikes page and for this to be saved
* Want the view hikes button to take me to a page with more information on that hike
* Want the view hike page to have useful data presented in a positive way
* Want the back button on view hikes to return me to my previous page
* Want the delete button to delete and remove hike data 

## Colour Scheme

Throughout the development of the project I tried to keep the colour scheme minimal with colours selected to reflect the outdoors hiking nature of the site.

I chose to have the text in the navbar white as it was clearly legible and looked good with the contrast of the green. The navbar itself was green (#639058) as this would be the start of the green outdoors theme for the website. The title and lead text on the landing page are also white as it again stands out positively from the scenic picture and is clear to read.

Throughout the website, the body background is a very faint green colour (#e3eae4). This fits nicely with the green outdoors theme, goes nicely with the header and makes the content very clear and easy to read for the user.

With the exception for the landing page, where the title is white on top of a scenic background image, each title on the rest of the website pages are (#a05709) which was a brown style to stand out from the content below but subtley keep with the outdoors theme.

The colour green (#639058) is used throughout the website. In addition to being the colour for the header, it is also used for the Edit button across various page and the border colour for the Add Hike/Edit Hike/View Hike content as well as the image and zoomed in map on the View Hike page. This was to keep consistency throughout the site.

On the Hikes page there are three buttons, the Edit button is the (#639058) green colour, the Delete button is a (#0980c5) blue colour to go with the blue water colour on the main Hikes map, and it has a hover colour of a (#f70b0b) red colour. The View hike button has a (#a05709) brown colour to match the title font colours.

## Features

The aim for this website was to make each page as simple as possible to navigate and understand. The font used across the website for titles, paragraph and button text is the Google font Montserrat as it looks nice and it clear for the reader. Sans-serif is availble for users who would not be able to view Montserrat.

The 'CRUD' operations was taken into account in developing this project, throughout the website it is possible for users to create, read, update and delete hike data.

### Navbar:

The navbar contains a brand logo in the top left corner for desktop and top centre for mobile and tablet, this also works as a link to the home page. Each of the links from the desktop navbar function without issue taking the user to the requested page. On tablet and mobile devices the navbar functions as a dropdown from a burger menu icon.

### Home Page:

The home page features a simple title with supporting text to give a concise description of the website purpose. This is presented above a scenic background image that dominates the page.

### Hikes Page:

Below the Hikes title is a map produced using Leaflet Maps using JavaScript. The default viewing position is to zoom in with the whole of the United Kingdom in focus with markers spread across the UK based on user input. As users fill in the add hikes form the option to provide coordinates adds a marker onto this map. Users can click each marker, this will have a Leaflets popup effect with the name of the hike, which also acts as a link to that hike page as well. This effect is effective across all devices. It is possible to zoom in and out of this map and scroll. 

Below the map the data input by the user on the Add Hikes page is displayed. Each piece of data is contains a simple white background with an Edit, Delete and View button for that hike and the town/city, county, and hike name inputted by the user. The rest of the data input by the user can be found by cicking the View button, in order to provide a clear page to display the data and to avoid the Hikes page becoming too overloaded with content as more hikes are added. The Edit Hikes button takes the user to the Edit Hike form, and the Delete button has an onclick popup feature to check whether the user wishes to proceed and delete the data. Each button has an on hover feature to change colour to make it clear to the user that each button is interactive.

There is also a very light green background for the body of the page and white backgrounds for the collapsible header and body to keep with a simple outdoors theme.

### View Hikes Page:

By clicking the View button next to the hike of the interest, the user is able to view more content regarding that hike. The data is all held within a green colored border box to contain the data neatly, with the exception of the user selected Hike Name which appears as the header of the page. On desktop and tablet the data is presented in two columns in the border box, with two columns of text going side by side. This text includes the County that the user selected from an optgroup dropdown feature, and the attributes taken from a multiple select dropdown. Each hike attribute displays the text and the corresponding well known logo by taking advantage of the Materialize collection feature.

Beneath the text, also side by side are the user selected URL image and a zoomed in map of the coordinates provided. The map coordinates are required on the add page form, but the image URL is optional, if the user chooses not to input a URL a default image stating 'No Image Found' is displayed to ensure the layout format is consistent.

Beneath the image and the map the Edit and Delete button are displayed, as well as a Back button. The Back button takes users back to the Hikes page.

On mobile view all the data remains contained within the colored border box, but each field is displayed on it's own line in one column to make it easier to read.

### Add Hikes Page:

The input form for the add hikes is within a green colored border box, in keeping with the simple green theme of the website. The border box is the same color and style as found on the View Hike page. On desktop and tablet these fields appear alongside each other with the exception of two taking the full width of the border box, on mobile each field is displayed on it's own line. The select country/county dropdown uses an optgroup feature from Materialize so that it is easier for the user to locate the county they are looking for based on the country of origin. A multiple input select dropdown was also used for hike attributes to save space on the page whilst still allowing the user choice. The hike name is a required field as it creates a unique ID for each hike zoomed in map. The coordinates input is also required as it adds a marker onto the main map on the top of the hikes page. The hike difficulty only allows numbers from 0-5 to ensure that all ratings remains within the same consistent grading system. The Add Hike button on the bottom of the page allows the user to add the data and they are then rerouted to the hikes page.

### Edit Hikes Page:

The Edit hikes follows the same layout format as the add hikes page to keep consistency. The selection choices are saved in case users only wish to amend one field. The Edit Hike button updates the hike data and reroutes the user to the hikes page.

The icons used on the input fields for both the Add Hike and Edit Hike pages were also taken from the Materialize. I found there was a slightly more limited choice of icons than if I had choosen an alterntiave such as Font Awesome used in the past, but there was enough to suit my purpose and I wanted to avoid adding additional dependencies into the project unnecessarily.

### Changes to Wireframes

The main difference from the original wireframe made at the start of the project was how the data was presented on the Hikes page. Originally the intention was to have all the hike data presented on the Hikes page using an accordian effect. Upon viewing this in action I decided it did not look as nice as it could, and it would result in numerous images and maps being loaded on one page unnecessarily. With this in mind I added a view button to each hike summary so that this data could be presented on a page by itself.

### Additional features to be implemented:

* I would like to add a feature to filter the hike selection by county name to narrow down the search field. I would like to do this for both hike data and the map markers.
* I would like to add in a log in authorisation feature to keep user data more protected against the risk of rogue users deleting all data
* Add an option for users to add photos from their personal device as opposed to URL

## Technologies Used

* HTML 5
* CSS
* JavaScript
* Python
* Flask
* Jinja
* PyMongo
* GitPod was the IDE used in the development of building this website.
* Materialize was used to aid the development process in the layout and responsiveness of the website.
* jQuery framework was used in conjunction with Materialize to refer to JavaScript technologies used to improve the efficiency of the website.
* MongoDB was the database used to host the website data
* The project was hosted on Heroku
* Google Fonts
* Leaflet Maps
* The W3C Mark Up Validation Service

## Testing

Each page has been run through an online validator, using the W3C Mark Up Validation Service.

## Code Validation

* I used the W3C HTML Validator tool to validate my HTML code. The W3C Validator tool doesn't recognise the Jinja templating, which resulted in it showing a lot of errors in relation to the Jinja code. However, all of the other code validates without error.
* I used the W3C CSS Validator tool to validate my CSS code.
* I used the JSHint tool to validate my JavaScript syntax. It found an error of an unused variable 'map', as this variable is declared inline on the 'hikes.html' page. There were also issues with it not recognising the Jinja templating.
* I used the Pep8 Online tool to validate my Python syntax. Had to update a number of lines that were too long and blank spaces I had initially missed.

### Navbar

The responsive Navbar was taken from the Materialize framework and amended to suit my needs. Each link within the navigation bar was tested across desktop to ensure that it took the user to the correct page without issue. On tablet and mobile devices the Navbar appears as a burgermenu dropdown feature, each link was tested within this device type also.

Each link is coded in the base.html page and uses jinja templating with Python functions applied in the app.py file. Each link was tested extensively to ensure the user could navigate to each page regardless of what page is active, fulfilling the user goal of navigation throughout the website. The brand logo is also routed to redirect the user to the home page, this is clear on the top left on desktop and is centred on tablet and mobile devices.


## Home Page

When testing the Home age across responsive devices it became apparent that the original image selected was not suitable for the purpose. Whilst being a positive scenic image it hindered the Home page title and lead text, making it difficult to read, especially on mobile. This was an issue as it meant the user to not have a clear idea of the website purpose upon viewing the home page. This was remedied with a different image and more focus being placed on ensuring the text is clear and legible. 

## About Page

No issues were faced with the About page. The linked within the navbar consistently worked as expected, and the one link within the text consistently takes the user to the intended destination (Google Maps) in a separate tab.

## Hikes Page

The Hikes page required frequest testing throughout development. The main feature of the page is a Leaflets Map at the top, which displays a marker on the coordinates that the user supplies for their hike, with a Leaflet popup with the user provided hike name when clicking on the marker. The map has a set default zoom and centre so that on all devices the UK is central and clear.

In the later stages of development a bug was disocvered with the map markers, in that if a user were to type a random assortment of characters into the coordinates input field this would be accepted and no map marker would appear. This also had a knock on effect of preventing any hikes input after this one from having their map marker displayed. To remedy this the required pattern for the coordinates input field was fixed so it would only accept the proper format, which is demonstrated for example on the About page. In addition to this a class of 'form-control validate' was added to the input tag as well as making it a required field. One issue raised by a test user was that it was not clear that there was content below the map on mobile, this was remedied with a media query stating to scroll down to view the hike data.

Each button, 'Edit', 'Delete' and 'View' were tested extensively on this page across all devices. As per the template routing using the Python functions in the app.py the 'Edit' button would always take the user the the Edit page for the ID of the hike they were selecting. The 'Delete' button would consistently remove the hike data immediately. After seeing how easy it could be to delete a hike in error an onclick feature was added to the button to confirm if the user wished to proceed. The 'View' button consistently would take to the user to a new page to view more information on the selected hike.

## Add Hike

The Country / County selection is a dropdown feature that shows all Counties within England, Scotland, Wales, Ireland and Northern Ireland. These counties are all presented by country in alphabetical order, this decision was made so that data would be separated by region and be easier to select. One bug that was encountered in testing was realising one county had been missed out and would not be in alphabetical order if added in late, to remedy this a sort feature was added within the jinja for loop for each country collection.

As previously mentioned an issue arose with the input for the add coordinates field as the input pattern initially used did not work apppropriately and opened the Hikes page to bugs with the markers on the Leaflets map. This was fixed by changing the input pattern.

A logical bug was discovered when one user tested the site and was able to select 6/5 as the difficulty for the hike. Whilst not affecting the functionality of the website it was a logical flaw, this was remedied by adding in a difficulty slider with minimum and maximum values applied.

Each required field has a * next to the label indicating this is an essential field, if a user fails to fill in one of these fields the Add Hike Button will not function and an altert will tell the user to fill in the selected field or to fill it in using the appropriate formart, as with the coorindates and the Hike Name.

## Edit Hike

The Edit Hike page was tested extensively to ensure that all data input by the user on the add hikes page would appear saved on the edit page. This initially proved an issue with the Attributes data as the options are not pulled from MongoDB but are added into the html of the Add Hikes page. To fix this issue a jinja if/else statement was applied to each attribute without using a for loop as with the Country / County selection dropdown.

Each required field has a * next to the label indicating this is an essential field, if a user fails to fill in one of these fields the Edit Hike Button will not function and an altert will tell the user to fill in the selected field or to fill it in using the appropriate formart, as with the coorindates and the Hike Name.

## View Hike Page

The View Hike data, as displayed by the wireframes, was initially intended to be included on the main Hikes page. The data input by the user was initially to be displayed in a collapsible body from the content that remains on the Hikes page. Included on the View Hike page is another Leaflets map zoomed in on the coordinates the user has input as well as a marker. Unfortunately this feature did not work within a collapsible body, unless devtools was opened and closed. After investigating this issue it appeared to be a resizing issue faced by many others online and after being unable to resolve it, it was necessary to display the map outside the collapsible body. This did not look good for the user when displayed, and gave me the realisation it would be better displayed on it's own page. This would also avoid users having to load all the images and maps for each hike on one page.

One bug that was encountered after a user testing the website was that they typed a longer than average Hike Name. This created issues on mobile view as the view page title pulls the data from Hike Name and had a fixed px font size, with the long page title forcing space on the right hand side. This was a simple fix of changing the font size type to em instead so it would be more responsive to the user device.

## Deployment

This project was developed using the GitPod IDE, committing to Git for every meaningful change and pushing commits to GitHub via the terminal Git commands. On GitHub I was able to view the Code Institute template reccomended for GitPod use, clone it, and then create my own repository with the template. After this it was possible to create a new workspace using GitPod.

### Local Deployment

In order for this project to be run locally, the user would require an IDE such as GitPod and the following features to be installed:

* Python3
* PIP
* Git would be required for version control throughout

Once you have met the above criteria you would be ready to clone this project to run locally. 

* At the top of the page clicking the green 'Clone or Download' gives you two otions to clone this GitHub repository. You can download the file as a zip-file and upload it into your new workspace, please ensure that you unzip the file first. Or alternatively you can copy the repository web URL, open the Git CLI terminal and type: git clone https://github.com/JonWil91/Milestone-3.git.
* Ensure you have navigated to the correct file location using the 'cd' command
* The next step would be to create a file named 'env.py', this will be an important file for safely storying your credentials. You would need to store your MONGO_URI and SECRET_KEY values within this file. After this create a '.gitignore' file with the only input being the name of the file with your credentials, 'env.py'. Ensure that your 'app.py' file searches for this path or the workspace won't be able to find the MONGO_URI data.
* The next required step would be ensuring you have an up to date requirements.txt file. This can be initialised by typing 'sudo -H pip3 -r requirements.txt' into the terminal, the syntax may differ slightly between IDE's as for use in GitPod the 'sudo' element was not required.

It would be necessary to create an account with MongoDB also so that you can develop your daatabase using MongoDB Atlas. Once you have created your account you would need to set up a database called 'hiking_database'. You would then need to create 6 collections within that database. A collection was created for England, Scotland, Wales, Republic of Ireland and Northern Ireland to ensure that each County was added carefully, as allowing users to add these in on the website could cause issues with duplication and typos.

The collection keeping all of the data added and edit by the user is the 'hikes' collection. The documents inserted into this are as follows:
* hike_region:
* county_name:
* hike_description:
* hike_difficulty
* hike_postcode:
* hike_duration:
* hike_distance:
* hike_name:
* multiple_selection: (this will be the only object returning as an array)
* hike_coordinates:
* img_url:

The Country collections should be completed as below:

eng_counties - Collection
eng_county - Object ID

irish_counties - Collection
irish_county - Object ID

north_ire_counties - Collection
north_ire_county - Object ID

scot_counties - Collection
scot_county - Object ID

wales_counties - Collection
wales_county - Object ID

Once these steps have been completed you have everything ready to run the application. If you are using the GitPod IDE you would run the command python3 app.py which will initialise the app and give you the prompt to expose the local host you are running and open it on a browser.

### Remote Deployment

This website has been deployed on Heroku using the master branch on GitHub. To host the project on Heroku the following steps were taken:

1. Sign up and create a free Heroku account and create a new app for later deployment
2. Create a requirements.txt file so that Heroku can install the necessary dependencies to run the app. In the CLI terminal type 'pip3 freeze --local > requirements.txt'
3. Create a Procfile which will tell Heroku what type of application is being deployed and how to run it. In the CLI terminal type 'echo web: python run.py > Procfile'
4. In Heroku after creating the project app, click the 'Deploy' tab, choose GitHub as your deployment method and select Enable Automatic Deployment.
5. Select the Settings tab next and click the 'Reveal Config Vars' button. You will then need to input the following details:
* IP: 0.0.0.0
* PORT: 8080
* MONGO_URI: <link to your MongoDB>
* MONGO_DBNAME: MongoDB database name
* SECRET_KEY: <your own secret key>

Once these steps have been followed you will be ready to deploy your website to Heroku.

## Credits 

### Media

* The default 'No Image Found' on the viewhike.html page in cases where the user does not provide a URL was taken from [Google Images](https://www.google.com/search?q=no+image+found&sxsrf=ALeKk037kfAGusljRBo7qXnd9969vrCcTw:1588604631821&source=lnms&tbm=isch&sa=X&ved=2ahUKEwijj5K2vZrpAhXJMMAKHZEuC8AQ_AUoAXoECAwQAw&biw=1920&bih=978#imgrc=lWVec5RfjFDSGM)
* [Leaflet Maps](https://leafletjs.com/) was used to provide the maps, tilelayers, attribution and markers across the website.
* The image on the home page is owned by me

### Code 

* env.py and .gitignore code was taken from Slack and Code Institute online mentors

## Acknowledgements

 A big thank you to my mentor, Gerry McBride for continued support and positive feedback throughout the project. A special thanks as well to all the Code Institute online support team









