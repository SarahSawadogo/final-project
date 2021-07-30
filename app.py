# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
import os
from model import worldList
from flask import redirect
from flask_pymongo import PyMongo


#  worldImageList
# -- Initialization section --
app = Flask(__name__)
app.config["MONGO_PASSWORD"] = os.getenv("MONGO_PASSWORD")

app.config["MONGO_DBNAME"] = 'globopedia'
# URI of database
app.config['MONGO_URI'] = f'mongodb+srv://admin:{app.config["MONGO_PASSWORD"]}@cluster0.ix55s.mongodb.net/globopedia?retryWrites=true&w=majority'

mongo = PyMongo(app)

# -- Routes section --


@app.route('/')
@app.route('/index.html')
def index():
    places = mongo.db.places
    places = places.find({})
    return render_template("index.html", time=datetime.now(), places=places)


@app.route('/add', methods=['GET', 'POST'])
def add():

    if request.method == 'GET':
        return render_template('index.html')

    else:
        # connect to the database
        places = mongo.db.places

        # insert new data

        des = request.form["des"]
        cdes = request.form["cdes"]
        img_url = request.form['img_url']
        places.insert({'des': des,
                      'cdes': cdes, 'img_url': img_url})

        # return a message to the user
        if des == "" or cdes == "" or img_url == "":
            return "Please fill out the form completely."

        else:
            message = "Thanks for your submission!"
            return render_template('submission.html', message=message, des=des, img_url=img_url)

        # return render_template('add.html', events = events)


# datetime.now() is used to trick browser to update faster
# add route for your gif results
@app.route('/countries_page.html', methods=["GET", "POST"])
def countries_page():
    try:
        selectedCountry = request.form['country'].lower()
        raw = worldList(selectedCountry)
        try:
            independence = raw["data"]["government"]["independence"]

        except:
            independence = {"date": "N/A", "note": "N/A"}

        print("happy")
        print(independence)

    except:
        return "404 error. Please enter the name of a country."

    return render_template("countries_page.html", time=datetime.now(), raw=raw, independence=independence)


@app.route('/countries/<country>')
def custom_countries(country):
    try:
        selectedCountry = country
        raw = worldList(selectedCountry)
        try:
            independence = raw["data"]["government"]["independence"]

        except:
            independence = {"date": "N/A", "note": "N/A"}

        print("happy")
        print(independence)

    except:
        return "404 error. Please enter the name of a country."

    return render_template("countries_page.html", time=datetime.now(), raw=raw, independence=independence)


@app.route('/maps.html')
def maps():
    return render_template("maps.html", time=datetime.now())


@app.route('/references.html')
def references():
    return render_template("references.html", time=datetime.now())
