import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'shopping_helper'
app.config["MONGO_URI"] = 'mongodb+srv://root:Pablo51@myfirstcluster-8ubao.mongodb.net/shopping_helper?retryWrites=true&w=majority'

mongo = PyMongo(app)
inventory_collection = mongo.db.inventory
categories_collection = mongo.db.categories
quantities_collection = mongo.db.quantities

@app.route("/")
@app.route("/get_items")
def get_items():
    return render_template("items.html", inventory=inventory_collection.find())

@app.route("/shopping_list")
def shopping_list():
    return render_template("shopping_list.html", inventory=inventory_collection.find({"$or": [{"quantity_name": "none"},{"quantity_name": "low"}]}))


@app.route('/add_item')
def add_item():
    return render_template("additem.html", categories=categories_collection.find(), quantities=quantities_collection.find())


@app.route('/insert_item', methods=['POST'])
def insert_item():
    items = inventory_collection
    items.insert_one(request.form.to_dict())
    return redirect(url_for('get_items'))


@app.route('/edit_item/<item_id>')
def edit_item(item_id):
    the_item = inventory_collection.find_one({"_id": ObjectId(item_id)})
    _categories = categories_collection.find()
    _quantities = quantities_collection.find()
    category_list = [category for category in _categories]
    quantity_list = [quantity for quantity in _quantities]
    return render_template("edititem.html", item=the_item, categories=category_list, quantities=quantity_list)


@app.route('/update_item/<item_id>', methods=['POST'])
def update_item(item_id):
    items = inventory_collection
    items.update( {'_id': ObjectId(item_id)},
    {
        'item_name': request.form.get('item_name'),
        'item_note': request.form.get('item_note'),
        'category_name': request.form.get('category_name'),
        'quantity_name': request.form.get('quantity_name')
    })
    return redirect(url_for('get_items'))


@app.route('/delete_item/<item_id>')
def delete_item(item_id):
    inventory_collection.remove({"_id": ObjectId(item_id)})
    return render_template("items.html", inventory=inventory_collection.find())


@app.route('/add_category')
def add_category():
    return render_template('addcategory.html', categories=categories_collection.find())


@app.route('/insert_category', methods=['POST'])
def insert_category():
    categories = mongo.db.categories
    categories.insert_one(request.form.to_dict())
    return redirect(url_for('add_category'))


@app.route('/edit_category/<item_id>')
def edit_category(item_id):
    the_category = categories_collection.find_one({"_id": ObjectId(item_id)})
    _categories = categories_collection.find()
    category_list = [category for category in _categories]
    return render_template("editcategory.html", category=the_category, categories=category_list)

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)