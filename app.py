# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
import os
from model import worldList
import random
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
    try:
        selectedCountry = request.form['country'].lower()
        raw = worldList(selectedCountry)
        try:
            independence =  raw["data"]["government"]["independence"]

        except:
            independence = {"date":"N/A", "note": "N/A"}
            
        print("happy")
        print(independence)
        
    except:
        return "404 error. Please enter the name of a country."
    
    return render_template("countries_page.html", time = datetime.now(), raw = raw, independence = independence)

@app.route('/countries/<country>')
def custom_countries(country):
    try:
        selectedCountry = country
        raw = worldList(selectedCountry)
        try:
            independence =  raw["data"]["government"]["independence"]

        except:
            independence = {"date":"N/A", "note": "N/A"}
            
        print("happy")
        print(independence)
        
    except:
        return "404 error. Please enter the name of a country."
    
    return render_template("countries_page.html", time = datetime.now(), raw = raw, independence = independence)


    

    
# def countries_image():
#     selectedCountries = request.form['country']
#     info = worldImageList(selectedCountries)

#     return render_template("countries_page.html", time = datetime.now(), info = info)
# def countries_page_img():
@app.route('/maps.html')
def maps():
    return render_template("maps.html", time = datetime.now())

@app.route('/references.html')
def references():
    return render_template("references.html", time = datetime.now())
