Milestone Project 3

# Let's Hike

This website is my third project after the culmination of studying Practial Python and Data Centric Development, including Flask and the MongoDB database system.

The website can be found at ...

## UX

This website was developed for users who have an interest in hiking within the United Kingdom. They will be greeted on the home page with a landing page picture with a simple title stating the purpose of the website. For more information on the purpose and benefit of the website users can visit the about page.
Users will be able to implement the CRUD system in order to add, view, edit and delete hikes with useful data presented for other hikers to visit those sites. Users can also visit a simple contact page if there is something that could or should be changed within the website.

## User stories:

As a user I would:

* Want to have a clear idea of the website purpose after visiting the home page
* Want to click the About button in the navbar and visit the About page
* Want to click the Hikes button in the navbar and visit the Hikes page
* Expect the Hikes page to have all existing Hikes displayed in a clear format
* Want to click the Add Hikes button in the navbar and visit the Add Hikes page
* Expect to be able to fill out a clear form on the Add Hikes page to add my data to the website

## Features

The aim for this website was to make each page as simple as possible to navigate and understand.

### Navbar:

The navbar contains a brand logo in the top left corner for desktop and top centre for mobile and tablet, this also works as a link to the home page. Each of the links from the desktop navbar function without issue taking the user to the requested page. On tablet and mobile devices the navbar functions as a dropdown from a burger menu icon.

### Home Page:

The home page features a simple title with supporting text to give a concise description of the website purpose. This is presented above a scenic background image that dominates the page.

### Hikes Page:

Below the Hikes title is a map produced using Leaflet Maps using JavaScript. The default viewing position is to zoom in with the whole of the United Kingdom in focus with markers spread across the UK based on user input. As users fill in the add hikes form the option to provide coordinates adds a marker onto this map. This effect is effective across all devices. It is possible to zoom in and out of this map and scroll. 

Below the map the data input by users is presented using the accordian effect with assistance from Materialize. On the collapsible header users will see an edit and delete button, clicking the edit button takes users to the edit hikes page, and clicking the delete button prompts users with a confirmation that they wish to delete the data for that hike. Alongside these buttons is the County of the hike that the user selects from an optgroup dropdown and the nearest town/city which the user types in. The final feature of the collapsible header is the icon signalling to users that it is a dropdown with more information available to view.

In the collapsible body users can view the various fields filled out on the add hike page. In addition to this, there is another map using Leaflet maps zoomed in on the coordinates provided on the add hike page. This map is responsive and displayed alongside the text on desktop and tablet, and underneath on mobile. It is possible to zoom in and out of this map and scroll.

There is also a very light green background for the body of the page and white backgrounds for the collapsible header and body to keep with a simple outdoors theme.

### Add Hikes Page:

The input form for the add hikes is within a green colored border box, in keeping with the simple green theme of the website. On desktop and tablet these fields appear alongside each other with the exception of two taking the full width of the border box, on mobile each field is displayed on it's own line. The select country/county dropdown uses an optgroup feature from Materialize so that it is easier for the user to locate the county they are looking for based on the country of origin. A multiple input select ticket box was also used for hike attributes to save space on the page whilst still allowing the user choice. The hike name is a required field as it creates a unique ID for each hike zoomed in map. The coordinates input also adds a marker onto the main map on the top of the hikes page. The Add Hike button on the bottom of the page allows the user to add the data and they are then rerouted to the hikes page.

### Edit Hikes Page:

The Edit hikes follows the same layout format as the add hikes page to keep consistency. The selection choices are saved in case users only wish to amend one field. The Edit Hike button updates the hike data and reroutes the user to the hikes page.

### Additional features to be implemented:

* I would like to add a feature to filter the hike selection by county name to narrow down the search field. I would like to do this for both hike data and the map markers.
* I would like to add in a log in authorisation feature to keep user data more protected against the risk of rogue users deleting all data
* Add an option for users to add photos

## Technologies Used

1. HTML
2. CSS
3. JavaScript
4. Python
5. Flask
6. Jinja
7. GitPod was the IDE used in the development of building this website.
8. Materialize was used to aid the development process in the layout and responsiveness of the website.
9. jQuery framework was used in conjunction with Materialize to refer to JavaScript technologies used to improve the efficiency of the website.
10. Google Fonts




