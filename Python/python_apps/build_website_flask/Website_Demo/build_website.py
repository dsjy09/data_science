#%% [markdown]

## This code is used to build a personal website using Flask in python

#%%
from flask import Flask, render_template
from flask.templating import render_template

# %%
app=Flask(__name__,template_folder='template')

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/travel/')
def travel():
    return render_template("travel.html")

if __name__=="__main__":
    app.run(debug=True)
# %%
