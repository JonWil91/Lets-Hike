import os
import bcrypt
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "hiking_database"

app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = 'mysecret'


mongo = PyMongo(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', hikes=mongo.db.hikes.find())

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/hikes')
def hikes():
    return render_template('hikes.html')

@app.route('/addhikes')
def addhikes():
    return render_template('addhikes.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
    SECRET_KEY = os.environ.get('mysecret')
