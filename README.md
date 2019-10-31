# Online Exam Registration System
		
	Online Exam Registration System is a project designed to make the Online Exam Registration 
	reliable with enhanced security. This system provides the student an efficient management 
	strategy to chose their exams. Online Exams has become a fast growing options for companies 
	because of its speed and accuracy. It needs less manpower to execute the examination. 
	
	Almost all organizations now-a-days, are conducting their exams online as it saves time for 
	student and get results in less time. It also helps the environment by saving paper. 
	In an online Exam Registration system, the user get userid and password by registering 
	their details in the site. This userId is used to authenticate the user when student login 
	to the site.
		
## UX

![](mockup/home.png)
	
	Mariam's Munch takes on a modern design by implementing features from the bootstrap.css framework.
	The application was designed to work just as well on devices with small screens as those with larger ones.

	All of the recipes on the home page are displayed on bootstrap cards, each showing a photo of the recipe, 
	the recipe title, description, duration and chef's name.
		
### Add Recipe

![](mockup/add-recipe.png)

	The user is redirected to this page when they would like to add a recipe of their own. 
	On this page their are a number of inputs that the user must fill in, it has intelligent labels and 
	icons to guide the user.

	The user can be as detailed or as simplistic as they would like to be when entering recipe ingredients. 
	The user has the option to add as many ingredients (with respective amounts) as they'd like.
	Similarly, the user can add as many steps in the method as they'd like to describe how to prepare 
	and cook the recipe.

	A dropdown is provided for the cuisine and the category.

### Edit Recipe

![](mockup/edit-recipe.png)
		
	This page mimics many of the properties of the add recipe page, to help the user identify 
	which fields they would like to update faster.

	If the user wants to save the changes, or discard them, buttons are displayed to guide the user.

### Delete Recipe

	The user also has the option to delete a recipe from the page, to prevent users accidentally 
	deleting recipes. An "Alert Popup" flashes asking the user to confirm their decision before the 
	recipe is permanently deleted from the database.
		
## FEATURES
	
	Existing features
		
	'COOK-BOOK'   - When the URL is entered it will always bring the user to the home page
	'Add Recipe'  - "Button" when clicked, it will allows the user to add new recipe
	'Search'      - "Button" when clicked, it will allows user to search recipes by Recipe Name.
	'Clear'       - "Button" when clicked, it will allows user to clear the Search.
	'View'        - "Button" when clicked, will bring to individual recipe page
	'Edit Recipe' - Click on the Image of the particular recipe and make changes by 
					clicking the "Button".
	'Remove'      - Click on the Image of the particular recipe and it has button to remove 
					particular recipe
	'Back'        - "Button" when clicked, will bring to back to home page from Edit recipe page.

	Features left to implement

	Feature that will allow user remove or edit(make changes) only its own recipes - 
	but not others users recipes.
	
## Technologies Used

	Git 
		This project uses command line to for regular commits and to push my project to github
	Github 
		This project uses to remotely store project code and allow public to see my website
	AWS
		This application is hosted via AWS
		
		
	Front-End Technologies:
	
	HTML
		This project uses HTML to build the foundation of the web application and 
		includes links to JS, CSS, and Font Awesome.
	CSS
		This project uses CSS to style the features of the web application and each 
		page of the cookbook.
	Bootstrap { Version 4.3.1 - (https://getbootstrap.com/docs/4.3.1/) }
		This project uses bootstrap for grid layout of the page.
	JQuery { Version: 3.3.1 }
		This project uses jQuery which is included with bootstrap to initialise many of the 
		bootstrap components used within the application.
	JavaScript
		This project uses JavaScript for interactive functionality of the application.
	Font Awesome
		This project uses Font Awesome to provide icons for the application.
		
		
	Back-End Technologies:
	
	Python { Version: 3.7.4 }
		This project uses Python to provide the backend functionality of the cookbook, 
		including functions to add, edit or delete a recipe.	
	PyMongo { Version: 3.9.0 }
		This project uses PyMongo which is a MongoDB driver for Python, used to access 
		the MongoDB database.
	JSON
		This project uses JSON to provide the core data for the cookbook, 
		including recipes, users, categories, etc.
	Flask { Version: 1.1.1 }
		This project uses the Flask microframework to bring the frontend and 
		backend of the application together.
	MongoDB
		This project uses MongoDB which is used to contain the database collections.
	Font Awesome
		This project uses Font Awesome to provide icons for the application.
	Jinja 
		This project uses to display back-end data to the front-end
	BSON ObjectId - 
		This project uses to allow to create and parse ObjectIDs without a reference to the 
		MongoDB or bson modules
		
			
## Testing

	1) Manual Tests
	
		This web application has been manually tested with different scenarios 
		that the user may experience.
		
		Homepage
		Enter the AWS URL it will be directed to homepage.
		
		Filter By Recipes Name
		Enter the RecipeName Click on 'SEARCH' button, the appropriate Recipe is filtered.
		
		Clear the Recipes Name
		Click on 'CLEAR' button, the search result of the Recipe is cleared.
		
		View Recipe
		Click on Image of the Recipe
		Be directed to the Recipe page and be shown all details of the recipe, 
		including the ingredients, method and image.
		
		Add Recipe
		Click on 'ADD RECIPE' button
		Fill in all details in the form and click 'SAVE RECIPE'.
		Be redirected to the homepage.
		
		Edit Recipe
		click on 'EDIT RECIPE' when viewing a recipe card.
		Edit any details within the form.
		Click on 'SAVE Recipe' and be redirected to homepage.
		Click on 'Back' and be redirected to homepage.
		
		Delete Recipe
		Click on 'REMOVE' when viewing a recipe card.
		It will show a pop up to confirm, once confirmed.
		The recipe will be deleted from the database.
		Return To Homepage
	
	2) Responsiveness Testing
	
		This application has been tested on all mobile, tablet and desktop screen sizes with 
		Google Chrome Developer Tools. From these tests, all issues have been resolved.

	3) Code Validation

		The HTML, CSS and JavaScript code for this application has been run through and 
		validated by bootstrap with JS.

## Deployment
	
The source code for this application can be found on [Github](https://github.com/maimbeeb/Cook-Book/) 
and the application itself has been deployed onto Heroku
There is no difference between the GitHub code and the code in the live application. 

It can be installed with the following steps:

 - Git Clone the repository
 - Install Heroku ToolBelt
 - From your command line, enter ```heroku``` to ensure heroku is installed 

    ```
    heroku login
    ```
 - Enter your credentials for heroku.com
    ```
    sudo pip3 install Flask
    sudo pip3 install pymongo
    sudo pip3 freeze --local > requirements.txt
    echo web: python run.py > Procfile
    git add .
    git commit -m "initial commit"
    git push -u heroku master
    ```
 - Application is live at Heroku.
	
## Credits
	
	Referred to the python documentation.
	Refered to the flask docs as well which have been a huge help.
	Thanks to mentor for planning and helping with the projects.
	A tutorial has been taken from Youtube.
	Many resources have been consulted online (stackoverflow, pyhton pep8, blogs, etc).
	
	Acknowledgements
	
	This project was based on a brief written by Code Institute to fulfil requirements of their Data 
	Centric Development module (part of the Full Stack Web Developer course).

