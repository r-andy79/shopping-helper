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
    return render_template("items.html", items=mongo.db.inventory.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)