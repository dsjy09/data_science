## This code is used to build a personal website using Flask in python

from flask import Flask, render_template
from flask.templating import render_template

import plotly
import plotly.graph_objs as go

import pandas as pd
import numpy as np
import json
import plotly.express as px

app=Flask(__name__,template_folder='template')

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# @app.route('/swiss/')
# def swiss():
#     return render_template("pages/swiss.html")

# @app.route('/travel/')
# def travel():
#     return render_template("pages/travel.html")

# @app.route('/videos/')
# def videos():
#     return render_template("pages/videos.html")

if __name__=="__main__":
    app.run(debug=True)