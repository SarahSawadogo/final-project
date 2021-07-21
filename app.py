# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
from model import getImageUrlFrom
import os

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", time = datetime.now())
#datetime.now() is used to trick browser to update faster

# add route for your gif results
@app.route('/yourgif', methods = ["GET", "POST"])

def yourgif():
    #get the gif from giphy and put it on webpage
    user_response = "dog"
    gifLink = getImageUrlFrom(user_response)
    print(gifLink)
    
    return render_template("yourgif.html", time = datetime.now(), gifLink = gifLink)