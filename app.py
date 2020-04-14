import os
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
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/hikes')
def hikes():
    _hikes = mongo.db.hikes.find()
    hike_list = [hike for hike in _hikes]
    _counties = mongo.db.counties.find()
    county_list = [county for county in _counties]
    return render_template('hikes.html', hikes = hike_list,
                                        counties = county_list)

@app.route('/addhikes')
def addhikes():
    _counties = mongo.db.counties.find()
    county_list = [county for county in _counties]
    return render_template('addhikes.html', counties = county_list)

@app.route('/insert_hikes', methods=['POST'])
def insert_hikes():
    hikes = mongo.db.hikes
    hikes.insert_one(request.form.to_dict())
    return redirect(url_for('hikes'))

@app.route('/edit_hike/<hike_id>')
def edit_hike(hike_id):
    the_hike =  mongo.db.hikes.find_one({"_id": ObjectId(hike_id)})
    all_counties =  mongo.db.counties.find()
    return render_template('edithike.html', hike=the_hike,
                            counties=all_counties)

@app.route('/update_hike/<hike_id>', methods=["POST"])
def update_hike(hike_id):
    hikes = mongo.db.hikes
    hikes.update({'_id': ObjectId(hike_id)},
    {
        'hike_region': request.form.get('hike_region'),
        'county_name': request.form.get('county_name'),
        'hike_description': request.form.get('hike_description'),
        'hike_difficulty': request.form.get('hike_difficulty'),
        'hike_parking': request.form.get('hike_parking'),
        'disabled_access': request.form.get('disabled_access'),
        'hike_postcode': request.form.get('hike_postcode'),
        'hike_duration': request.form.get('hike_duration'),
        'hike_distance': request.form.get('hike_distance'),
        'hike_coordinates': request.form.get('hike_coordinates')
    })
    return redirect(url_for('hikes'))

@app.route('/delete_hike/<hike_id>')
def delete_hike(hike_id):
    mongo.db.hikes.remove({'_id': ObjectId(hike_id)})
    return redirect(url_for('hikes'))

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
