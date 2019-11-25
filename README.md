# Shopping Helper Application

Third Milestone Project - Data-Centric Development - Code Institute

The aim of Shopping Helper application is to help managing household's food supplies and groceries shopping. Application consists of to main sections: Supply inventory and a Shopping list. User can add products to the inventory, specifying their name, category and quantity. If the amount of a certain product is low or none, it will show up on a Shopping list. User can also add new categories and edit them.

Existing features:
* adding items to supply inventory,
* editing and removing existing items
* filtering items based on quantities of the products (shopping list)
* searching the database to check if item exists in inventory,
* 

## User stories

* As a user I want to be able to add products to the database, specifying their current quantity, category and adding a short note
* As a user I want to be able to search the database, to see if I'm in possession of certain product
* As a user I want to be able to monitor quantity of different products that I have
* As a user I want to be able to update the details of owned products, such as: name, note, quantity, category
* As a user I want to be able to add new categories to the database

## Features
The purpose of the app is to help managing household supplies by keeping track of posessed goods and create shopping list based on the quantities of products. User can add the products he/she has in their storage using 'Add item' form and specifying item's name, category, quantity. A short note can also be added. Apart from these four values, current timestamp is also being added to the database. User can choose from 4 quantities that will be assigned to the product: full, safe amount, low and none. If quantity of product is 'low' or 'none', the item will display on the 'Shopping list'. Products are ordered by the category. User can view what products are under specific category by clicking on it.
Shopping list shows the products which quantity is either 'low' or 'none'. When doing shopping, user can tap on 'Bought' button whenever an item is placed in the basket. This will remove item from the list and will change its quantity to 'full'.

## Testing

## Technologies used
Application was built using using the following technologies:
* Python
* Flask framework
* Materialize CSS library
* Jinja templating language
* jQuery library
* HTML
* CSS

## Deployment

## Acknowledgements