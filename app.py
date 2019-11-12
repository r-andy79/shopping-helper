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
    return render_template('additem.html', categories=categories_collection.find(), quantities=mongo.db.quantities.find())


@app.route('/insert_item', methods=['POST'])
def insert_item():
    items = mongo.db.inventory
    items.insert_one(request.form.to_dict())
    return redirect(url_for('get_items'))


@app.route('/edit_item/<item_id>')
def edit_item(item_id):
    the_item = inventory_collection.find_one({"_id": ObjectId(item_id)})
    the_category = mongo.db.categories.find()
    return render_template('edititem.html', item=the_item, category=the_category)


@app.route('/add_category')
def add_category():
    return render_template('addcategory.html', categories=categories_collection.find())


@app.route('/insert_category', methods=['POST'])
def insert_category():
    categories = mongo.db.categories
    categories.insert_one(request.form.to_dict())
    return redirect(url_for('get_items'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)