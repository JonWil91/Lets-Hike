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

mongo = PyMongo(app)

@app.route('/')
@app.route('/home_hikes')
def home_hikes():
    return render_template('index.html', hikes=mongo.db.hikes.find())

@app.route('/about_me')
def about_me():
    return render_template('aboutme.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login')
def login():
    if 'username' in session:
        return 'You are logged in as ' + session['username']

    return render_template('login.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)