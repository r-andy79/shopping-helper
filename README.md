# Shopping Helper Application

Third Milestone Project - Data-Centric Development - Code Institute

The aim of Shopping Helper application is to help managing household's food supplies and optimize groceries shopping. Application consists of two main sections: Supplies Inventory and a Shopping List. User can add products to the inventory, specifying their name, category and quantity. If the amount of a certain product is set to 'low' or 'none', the item will appear on a Shopping list. User can also add new categories and edit them. I don't like preparing shopping lists, as I always forget to put something on it or I end up buying products that I already have, but I don't remember about that fact. The goal of the application is to prevent 'overbuying' products and waste less food. This can be achieved by keeping the information in the database up-to-date.

## UX
The applcation can serve anyone in their day-to-day shopping. It can help the user to monitor current amounts of products in their kitchen/storage and automatically create shopping list based on that information. If the information in the database is accurate, it should help users optimize their shopping.

### User stories
---
* As a user I want to be able to add products to the database, specifying their current quantity, category and adding a short note
* As a user I want to be able to search the database, to see if I'm in possession of certain product
* As a user I want to be able to monitor quantity of different products that I have
* As a user I want to be able to update the details of owned products, such as: name, note, quantity, category
* As a user I want to be able to add new categories to the database

Shopping Helper uses a database that consists of three collections:
- Inventory collection,
- Categories collection,
- Quantities collection,

The categories and quantities collections are nested in the inventory collection. New documents can be added to the categories collection and modified as well. The quantities collection has four predefined documents that represent states and cannot be altered by the user. The inventory collection is created by user, based on the information on the products they own (or lack) in their kitchen/storage. Please see the database schema below:

![Shopping Helper application database schema](wirefarems/database_schema.png)

[Here](wireframes/) you can find wireframes for different views of the application across various devices:
- desktop / laptop,
- tablet,
- smartphone



Existing features:
* adding items to the inventory,
* editing and removing existing items,
* filtering items based on quantities of the products (shopping list)
* searching the database to check if item exists in inventory,
* 

## Features

### Existing features

The purpose of the app is to help managing household supplies by keeping track of posessed goods and create shopping list based on the quantities of products. User can add the products he/she has in their storage using 'Add item' form and specifying item's name, category, quantity. A short note can also be added. Apart from these four values, current timestamp is also being added to the database. User can choose from 4 quantities that will be assigned to the product: full, safe amount, low and none. If quantity of product is 'low' or 'none', the item will display on the 'Shopping list'. Products are ordered by the category. User can view what products are under specific category by clicking on it.
Shopping list shows the products which quantity is either 'low' or 'none'. When doing shopping, user can tap on 'Bought' button whenever an item is placed in the basket. This will remove item from the list and will change its quantity to 'full'.

### Features left to implement


## Technologies used
Application was built using using the following technologies:
* Python
* Flask framework
* Materialize CSS library
* Jinja templating language
* jQuery library
* HTML
* CSS

## Testing

## Deployment

## Acknowledgements