## This code is used to build a personal website using Flask in python

from flask import Flask, render_template
from functions import *
import base64

app=Flask(__name__,template_folder='template')

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/work')
def work():
    outputs=get_medium_articles()
    return render_template("work.html", outputs=outputs)

@app.route('/travel')
def travel():

    plot_html=mapplot()
    return render_template("travel.html",plot_html=plot_html)

@app.route('/blog')
def blog():
    return render_template("blog.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/test')
def test():
    return render_template("swiss.html")

# @app.route('/travel/')
# def travel():
#     return render_template("pages/travel.html")



# @app.route('/<string:page_name>')
# def html_page(page_name):
#     return render_template(page_name)


# def get_flask_output():
#     return "Hello, this is the output from Flask!"

# @app.route('/<string:page_name>')
# def work(page_name):
#     output='give a try'
#     return render_template(page_name, outputs=output)





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