# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
import os
from model import worldList

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
    selectedCountry = request.form['country']
    data = worldList(selectedCountry)
    
    
    return render_template("countries_page.html", time = datetime.now(), data = data)

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
