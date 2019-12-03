import os
import datetime
from flask import Flask, flash, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'shopping_helper'
app.config["MONGO_URI"] = 'mongodb+srv://root:Pablo51@myfirstcluster-8ubao.mongodb.net/shopping_helper?retryWrites=true&w=majority'
app.secret_key = 'some random text'

mongo = PyMongo(app)
inventory_collection = mongo.db.inventory
categories_collection = mongo.db.categories
quantities_collection = mongo.db.quantities

def group_by_category(products):
    """Function allowing to group the products by category"""
    categories = {}
    for p in products:
        i = p['_id']
        c = p['category_name']
        n = p['item_name']
        q = p['quantity_name']
        d = p['date_added']
        note = p['item_note']
        
        if not categories.get(c):
            categories[c] = []
        x = {'id': i, 'name': n, 'quantity': q, 'note': note, 'category': c, 'date': d}
        categories[c].append(x)
    return categories

@app.template_filter('datetimeformat')
def datetimeformat(value, format='%d-%m-%Y'):
    """Filter for formatting the date in the application"""
    return value.strftime(format)

@app.route("/")
@app.route("/get_items")
def get_items():
    """Function responsible for the main view of the application, displays all items in the database grouped by category"""
    inventory=inventory_collection.find()
    grouped_items = group_by_category(inventory)
    return render_template("items.html", grouped_items=grouped_items)

@app.route("/shopping_list")
def shopping_list():
    """Shopping list view displays items where quantity is 'low' or 'none'"""
    inventory=inventory_collection.find({"$or": [{"quantity_name": "none"},{"quantity_name": "low"}]})
    grouped_items = group_by_category(inventory)
    return render_template("shopping_list.html", grouped_items=grouped_items)


@app.route('/add_item')
def add_item():
    """Add new item view allows user to access the form collecting information about new items"""
    return render_template("additem.html", categories=categories_collection.find(), quantities=quantities_collection.find())


@app.route('/search_item', methods=['GET', 'POST'])
def search_item():
    """Search item view allows user to search the database using product name"""
    search_item = request.form.get('item_name')
    results=inventory_collection.find({"item_name": {"$regex": search_item}})
    results_list = [result for result in results]
    return render_template("search_results.html", results=results_list)


@app.route('/insert_item', methods=['POST'])
def insert_item():
    """Allows user to insert new item to the database"""
    items = inventory_collection
    form = request.form.to_dict()
    items.insert_one({
      "item_name": form["item_name"],
      "item_note": form["item_note"],
      "category_name": form["category_name"],
      "quantity_name": form["quantity_name"],
      "date_added": datetime.datetime.now()
    }
    )
    flash('An item has been added')
    return redirect(url_for('get_items'))


@app.route('/edit_item/<item_id>')
def edit_item(item_id):
    """Allows user to edit an existing item"""
    the_item = inventory_collection.find_one({"_id": ObjectId(item_id)})
    _categories = categories_collection.find()
    _quantities = quantities_collection.find()
    category_list = [category for category in _categories]
    quantity_list = [quantity for quantity in _quantities]
    return render_template("edititem.html", item=the_item, categories=category_list, quantities=quantity_list)


@app.route('/update_item/<item_id>', methods=['POST'])
def update_item(item_id):
    """Updates the specified item information in the database"""
    items = inventory_collection
    items.update( {'_id': ObjectId(item_id)},
    {"$set":
      {
        'item_name': request.form.get('item_name'),
        'item_note': request.form.get('item_note'),
        'category_name': request.form.get('category_name'),
        'quantity_name': request.form.get('quantity_name')
      }
    })
    flash('An item has been updated')
    return redirect(url_for('get_items'))


@app.route('/buy_item/<item_id>', methods=['GET', 'POST'])
def buy_item(item_id):
    """Updates item quantity to 'full' when an item has been bought. As a result the item is no longer displayed on the shopping list"""
    items = inventory_collection
    items.update({'_id': ObjectId(item_id)},
    {"$set":
        {
            'quantity_name': "full",
            'date_added': datetime.datetime.now()
        }
    })
    return redirect(url_for('shopping_list'))


@app.route('/delete_item/<item_id>')
def delete_item(item_id):
    """Deletes specified item from the database"""
    inventory_collection.remove({"_id": ObjectId(item_id)})
    flash('Item has been removed')
    return redirect(url_for('get_items'))


@app.route('/add_category')
def add_category():
    """Add category view allows user to access the form collecting information about new categories and displays the existing categories"""
    return render_template('addcategory.html', categories=categories_collection.find())


@app.route('/insert_category', methods=['POST'])
def insert_category():
    """Inserts new category into the database"""
    categories = mongo.db.categories
    categories.insert_one(request.form.to_dict())
    return redirect(url_for('add_category'))


@app.route('/edit_category/<item_id>')
def edit_category(item_id):
    """Allows user to edit the name of an existing category"""
    the_category = categories_collection.find_one({"_id": ObjectId(item_id)})
    _categories = categories_collection.find()
    category_list = [category for category in _categories]
    return render_template("editcategory.html", category=the_category, categories=category_list)


@app.route('/update_category/<item_id>', methods=['POST'])
def update_category(item_id):
    """Updates the category name in the database in Category and Inventory collection"""
    current_category_name = categories_collection.find_one({'_id': ObjectId(item_id)})['category_name']
    print(current_category_name)
    inventory = inventory_collection
    inventory.update({'category_name': current_category_name},
    {"$set":
      {
        'category_name': request.form.get('category_name')
      }
    } 
    )
    categories = categories_collection
    categories.update( {'_id': ObjectId(item_id)},
    {
        'category_name': request.form.get('category_name')
    })
    return redirect(url_for('add_category'))


@app.errorhandler(404)
def not_found(error):
    """Displays an error page in case the desired page is not found"""
    return render_template('404.html')

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)