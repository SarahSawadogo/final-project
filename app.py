# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
import os
from model import worldList, city
#  worldImageList
# -- Initialization section --
app = Flask(__name__)
app.config["GIPHY_KEY"] = os.getenv("GIPHY_KEY")
# -- Routes section --
@app.route('/')
@app.route('/index.html')
def index():
    return render_template("index.html", time = datetime.now())
#datetime.now() is used to trick browser to update faster
# add route for your gif results
@app.route('/countries_page.html', methods = ["GET", "POST"])
def countries_page():
    selectedCountry = request.form['country'].lower()
    raw = worldList(selectedCountry)

    return render_template("countries_page.html", time = datetime.now(), raw = raw)

# def countries_image():
#     selectedCountries = request.form['country']
#     info = worldImageList(selectedCountries)

#     return render_template("countries_page.html", time = datetime.now(), info = info)
# def countries_page_img():
@app.route('/maps.html')
def maps():
    return render_template("maps.html", time = datetime.now())
@app.route('/aboutUs.html')
def aboutUs():
    return render_template("aboutUs.html", time = datetime.now())
@app.route('/references.html')
def references():
    return render_template("references.html", time = datetime.now())
@app.route('/signIn.html')
def signIn():
    return render_template("signIn.html", time = datetime.now())

# city image routes    
@app.route('/argentina.html')
def argentina():
    return render_template("argentina.html", time = datetime.now())

@app.route('/australia.html')
def australia():
    return render_template("australia.html", time = datetime.now())

@app.route('/cambodia.html')
def cambodia():
    return render_template("cambodia.html", time = datetime.now())

@app.route('/canada.html')
def canada_page():
    country_name_one = "canada"
    can = city(country_name_one)
    return render_template("canada.html", time = datetime.now(), can = can)

@app.route('/chile.html')
def chile():
    return render_template("chile.html", time = datetime.now())

@app.route('/fiji.html')
def fiji():
    return render_template("fiji.html", time = datetime.now())

@app.route('/mexico.html')
def mexico():
    return render_template("mexico.html", time = datetime.now())

@app.route('/morocco.html')
def morocco():
    return render_template("morocco.html", time = datetime.now())

@app.route('/netherland.html')
def netherland():
    return render_template("netherland.html", time = datetime.now())

@app.route('/newZealand.html')
def newZealand():
    return render_template("newZealand.html", time = datetime.now())

@app.route('/nicaragua.html')
def nicaragua():
    return render_template("nicaragua.html", time = datetime.now())

@app.route('/phillipines.html')
def phillipines():
    return render_template("phillipines.html", time = datetime.now())

@app.route('/saudiArabia.html')
def saudiArabia():
    return render_template("saudiArabia.html", time = datetime.now())

@app.route('/somalia.html')
def somalia():
    return render_template("somalia.html", time = datetime.now())

@app.route('/south_africa.html')
def south_africa():
    return render_template("south_africa.html", time = datetime.now())

@app.route('/switzerland.html')
def switzerland():
    return render_template("switzerland.html", time = datetime.now())

@app.route('/ukraine.html')
def ukraine():
    return render_template("ukraine.html", time = datetime.now())

@app.route('/uruguay.html')
def uruguay():
    return render_template("uruguay.html", time = datetime.now())


