import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'shopping_helper'
app.config["MONGO_URI"] = 'mongodb+srv://root:Pablo51@myfirstcluster-8ubao.mongodb.net/shopping_helper?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route("/")
@app.route("/get_items")
def get_items():
    return render_template("items.html", inventory=mongo.db.inventory.find())

@app.route("/shopping_list")
def shopping_list():
    return render_template("shopping_list.html", inventory=mongo.db.inventory.find({"$or": [{"quantity_name": "none"},{"quantity_name": "low"}]}))


@app.route('/add_item')
def add_item():
    return render_template('additem.html', categories=mongo.db.categories.find(), quantities=mongo.db.quantities.find())


@app.route('/insert_item', methods=['POST'])
def insert_item():
    items = mongo.db.inventory
    items.insert_one(request.form.to_dict())
    return redirect(url_for('get_items'))


@app.route('/add_category')
def add_category():
    return render_template('addcategory.html', categories=mongo.db.categories.find())


@app.route('/insert_category', methods=['POST'])
def insert_category():
    categories = mongo.db.categories
    categories.insert_one(request.form.to_dict())
    return redirect(url_for('get_items'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)