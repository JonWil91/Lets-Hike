import os
from flask import Flask, render_template, redirect, request, url_for
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
    _engcounties = mongo.db.eng_counties.find()
    eng_county_list = [engcounty for engcounty in _engcounties]
    _scotcounties = mongo.db.scot_counties.find()
    scot_county_list = [scotcounty for scotcounty in _scotcounties]
    _walescounties = mongo.db.wales_counties.find()
    wales_county_list = [walescounty for walescounty in _walescounties]
    _irishcounties = mongo.db.irish_counties.find()
    irish_county_list = [irishcounty for irishcounty in _irishcounties]
    _northirishcounties = mongo.db.north_ire_counties.find()
    north_ire_county_list = [northirishcounty for northirishcounty
                             in _northirishcounties]
    for hike in hike_list:
        print(hike['hike_name'])
    return render_template('hikes.html', hikes=hike_list,
                           engcounties=eng_county_list,
                           scotcounties=scot_county_list,
                           walescounties=wales_county_list,
                           irishcounties=irish_county_list,
                           northirishcounties=north_ire_county_list)


@app.route('/addhikes')
def addhikes():
    _engcounties = mongo.db.eng_counties.find()
    eng_county_list = [engcounty for engcounty in _engcounties]
    _scotcounties = mongo.db.scot_counties.find()
    scot_county_list = [scotcounty for scotcounty in _scotcounties]
    _walescounties = mongo.db.wales_counties.find()
    wales_county_list = [walescounty for walescounty in _walescounties]
    _irishcounties = mongo.db.irish_counties.find()
    irish_county_list = [irishcounty for irishcounty in _irishcounties]
    _northirishcounties = mongo.db.north_ire_counties.find()
    north_ire_county_list = [
        northirishcounty for northirishcounty in _northirishcounties]
    return render_template('addhikes.html', engcounties=eng_county_list,
                           scotcounties=scot_county_list,
                           walescounties=wales_county_list,
                           irishcounties=irish_county_list,
                           northirishcounties=north_ire_county_list)


@app.route('/insert_hikes', methods=['POST'])
def insert_hikes():
    hike = {
        'hike_region': request.form.get('hike_region'),
        'county_name': request.form.get('county_name'),
        'hike_description': request.form.get('hike_description'),
        'hike_difficulty': request.form.get('hike_difficulty'),
        'hike_postcode': request.form.get('hike_postcode'),
        'hike_duration': request.form.get('hike_duration'),
        'hike_distance': request.form.get('hike_distance'),
        'hike_name': request.form.get('hike_name'),
        'hike_coordinates': request.form.get('hike_coordinates'),
        'multiple_selction': request.form.getlist('multiple_selction'),
        'img_url': request.form.get('img_url')
    }
    mongo.db.hikes.insert_one(hike)
    return redirect(url_for('hikes'))


@app.route('/edit_hike/<hike_id>')
def edit_hike(hike_id):
    the_hike = mongo.db.hikes.find_one({"_id": ObjectId(hike_id)})
    eng_counties = mongo.db.eng_counties.find()
    scot_counties = mongo.db.scot_counties.find()
    wales_counties = mongo.db.wales_counties.find()
    irish_counties = mongo.db.irish_counties.find()
    north_ire_counties = mongo.db.north_ire_counties.find()
    return render_template('edithike.html', hike=the_hike,
                           engcounties=eng_counties,
                           scotcounties=scot_counties,
                           walescounties=wales_counties,
                           irishcounties=irish_counties,
                           northirishcounties=north_ire_counties)


@app.route('/update_hike/<hike_id>', methods=["POST"])
def update_hike(hike_id):
    hikes = mongo.db.hikes
    hikes.update({'_id': ObjectId(hike_id)},
                 {
        'hike_region': request.form.get('hike_region'),
        'county_name': request.form.get('county_name'),
        'hike_description': request.form.get('hike_description'),
        'hike_difficulty': request.form.get('hike_difficulty'),
        'hike_postcode': request.form.get('hike_postcode'),
        'hike_duration': request.form.get('hike_duration'),
        'hike_distance': request.form.get('hike_distance'),
        'hike_name': request.form.get('hike_name'),
        'multiple_selction': request.form.getlist('multiple_selction'),
        'hike_coordinates': request.form.get('hike_coordinates'),
        'img_url': request.form.get('img_url')
    })
    return redirect(url_for('hikes'))


@app.route('/delete_hike/<hike_id>')
def delete_hike(hike_id):
    mongo.db.hikes.remove({'_id': ObjectId(hike_id)})
    return redirect(url_for('hikes'))


@app.route('/hikes/view/<hike_id>')
def view_hike(hike_id):
    the_hike = mongo.db.hikes.find_one({"_id": ObjectId(hike_id)})
    return render_template('viewhike.html', hike=the_hike)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)
