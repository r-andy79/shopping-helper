# Shopping Helper Application

Third Milestone Project - Data-Centric Development - Code Institute

The aim of Shopping Helper application is to help managing household's food supplies and optimize groceries shopping. Application consists of two main sections: Supplies Inventory and a Shopping List. User can add products to the inventory, specifying their name, category and quantity. If the amount of a certain product is set to 'low' or 'none', the item will appear on a Shopping list. User can also add new categories and edit them. I don't like preparing shopping lists, as I always forget to put something on it or I end up buying products that I already have, but I don't remember about that fact. The goal of the application is to prevent 'overbuying' products and waste less food. This can be achieved by keeping the information in the database up-to-date. Once the products are input in the database, they can be updated 'on-the-go' as they are being consumed. This can save us time, as we don't have to prepare shopping lists every time we go shopping, but they are being created incrementally.
I wanted to build an application that would be useful to me in my everyday life and help me to save time and waste less food.

Table of contents:
- [Overview](#shopping-helper-application)
- [UX](#ux)
- [User stories](#user-stories)
- [Features](#features)
  - [Existing features](#existing-features)
  - [Features left to implement](#features-left-to-implement)
- [Technologies used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Acknowledgements](#acknowledgements)

## UX
The applcation can serve anyone in their day-to-day shopping. It can be used by a single user, or a household / community members. It can help the user(s) to monitor current amounts of products in their kitchen/storage and automatically create shopping list based on that information. Provided the information in the database is accurate, it should help users optimize their shopping.

I wanted the user interface to be simple and consistent throughout the whole application. The data is presented in a clean and organized way. User has easy access to all the functions from the navigation bar on larger screens or a mobile menu that is triggered by the 'hamburger' button.

### User stories

* As a user I want to be able to add products to the database, specifying their current quantity, category and adding a short note,
* As a user I want to be able to add a new category,
* As a user I want to be able to edit an existing category,
* As a user I want to be able to view the shopping list, to see what I need to buy,
* As a user I want to be able to search the database, to see if I'm in possession of a certain product,
* As a user I want to be able to monitor quantity of different products that I own,
* As a user I want to be able to update the details of owned products, such as: name, note, quantity, category,
* As a user I want to be able to delete products from the database,
* As a user I want to be able to check when the item had been previously bought,
* As a user I want to be able to remove items from the shopping list after buying them
* As a user I want to be able to do shopping by department

Shopping Helper uses a database that consists of three collections:
- Inventory collection,
- Categories collection,
- Quantities collection,

The categories and quantities collections are nested in the inventory collection. New documents can be added to the categories collection and modified as well. The quantities collection has four predefined documents that represent states and cannot be altered by the user. The inventory collection is created by user, based on the information on the products they own (or lack) in their kitchen/storage. Please see the database schema below:

![Shopping Helper application database schema](wireframes/database_schema.png)

[Here](wireframes/) you can find wireframes for different views of the application across various devices:
- desktop / laptop,
- tablet,
- smartphone


## Features

The application has a number of features that are described below:

### Existing features:

- [x] Feature 1 - allows users to add products to the database, by having them fill out the form under 'Add Item' link from the navigation bar / mobile menu,
- [x] Feature 2 - allows users to add new categories, by having them fill out the form under 'Add / Edit Category' link from the navigation bar / mobile menu,
- [x] Featire 3 - allows users to edit existing categories, by having them click the 'Edit' button next to category name,
- [x] Feature 4 - allows users to view the shopping list, by clicking / tapping on the 'Shopping List' link from the navigation bar / mobile menu,
- [x] Feature 5 - allows users to search for products in the database, by having them fill out the search form in the main application view,
- [x] Feature 6 - allows users to monitor quantity of different products, by clicking / tapping on specific categories in the main application view,
- [x] Feature 7 - allows users to update the information about the products by clicking / tapping the 'Edit' button, located to the right of product info in the main application view,
- [x] Feature 8 - allows users to remove products from the database by clicking / tapping the 'Remove' button, located to the right of the product info in the main application view,
- [x] Feature 9 - allows users to check when the item had been previously bought. This information is shown in the product info of the main application view,
- [x] Feature 10 - allows users to remove items from the 'Shopping list' by clicking the 'Bought' button, next to the item details in the Shopping List view. It is done by updating the product quantity to 'full'
- [x] Feature 11 - allows users to do their shopping by department. It is achieved by listing the products on the shopping list by category.

### Features left to implement:

- [ ] Form validation - currently app has no forms validation
- [ ] Login functionality

Users can add the products they have in their storage using 'Add item' form and specifying item's name, category, quantity. A short note can also be added. Apart from these four values, current timestamp is also being added to the database. User can choose from 4 quantities that will be assigned to the product: full, safe amount, low or none. If quantity of product is 'low' or 'none', the item will display on the 'Shopping list'. Products are ordered by category. User can view products that are under specific category by clicking on it in the main application screen.
Shopping list shows the products with quantities 'low' or 'none'. When doing shopping, user can tap on 'Bought' button whenever an item is placed in the basket. This will remove item from the list and will change its quantity to 'full'.

## Technologies used
Application was built using using following technologies:
* [Python](https://www.python.org/) - used for general-purpose programming and writing the logic of the application,
* [Flask framework](http://flask.palletsprojects.com/en/1.1.x/) - used for serving templates, performing CRUD operations
* [MongoDB](https://www.mongodb.com/) - used for storing the application data,
* [Materialize CSS library](https://materializecss.com/) - used for building the visual side of the application,
* [Jinja templating language](https://jinja.palletsprojects.com/en/2.10.x/) - used for incorporating Python code into HTML templates,
* [jQuery library](https://jquery.com/) - used for triggering functions required by the Materialize library,
* [HTML](https://html.spec.whatwg.org/) - used for building the structure of the interface,
* [CSS](https://docs.ckan.org/en/ckan-2.7.3/contributing/css.html) - used for custom styling of some elements

## Testing
Application has been tested across different devices:
* desktop,
* laptop,
* tablet,
* smartphone,

as well as different browsers:

* Google Chrome (desktop & mobile),
* Mozilla Firefox (desktop),
* Microsoft Edge (desktop),
* Brave (mobile).

Application works correctly across different screen and resolutions, as well as the orientations.

Aplication functions have been tested to ensure they work correctly:

* CRUD operations - all functions work correctly, aplication retrieves data from the database with no issues. New items can be added, as well as being updated and deleted from the database.
* Search input searches the database and returns the results or provides a message to the user in case there are no matching results,

Unit tests were written and are located in [tests.py](tests.py) file. These test are meant to prove if the templates are displayed correctly. They can be run by typing `python3 tests.py`. The tests ran successfully and results can be found [here](wireframes/test_screenshot.png).


## Deployment

Application has been deployed to Heroku platform and is available under [this link](http://shopping-helper-app.herokuapp.com/). In order to deploy the application to Heroku, the following steps were followed:
1. Log in to [Heroku](https://www.heroku.com/) platform,
2. Create a new app,
3. Log in to Heroku from the terminal of your editor/platform using your credentials,
4. Create `requirements.txt` file using `sudo pip3 freeze --local > requirements.txt` command,
5. Create a `Procfile` using `echo web: python app.py > Procfile` command,
6. Initialize new Git repository, by inputting `git init`,
7. Add the files to the repository, by inputting `git add .`,
8. Commit the changes to the repository, by inputting `git commit -m 'Initial commit'`,
9. Associate the Heroku application as a branch of the repository by inputting `heroku git:remote -a shopping-helper-app`,
10. Push the application to Heroku, by inputting `git push heroku master`,
11. Run the application using `heroku ps:scale web=1`,
12. Specify IP and PORT as config vars in Heroku app setting

There are no differences between deployed and development version of the application.

The repository of the application is available on the master branch on [GitHub](https://github.com/r-andy79/shopping-helper). New functions were built on new branches and merged with master branch, after they had been tested successfully.

## Acknowledgements

The idea for the application comes from the 'To-do list' mini project from the Data-Centric Development module. 