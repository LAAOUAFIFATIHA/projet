from flask import Flask,render_templates
Flask.make_response
from flask import make_response
from flask import Flask, url_for
#elle prend comme argumment la fonction de vue 
app = Flask (__name__)


app = Flask (__name__)



def saysalam():
    return """<a href="%s">routeur a la page d'accueil</a>"""%url_for('root')

#_______________greeting_______________#
@app.route("/greeting")
def greeting ():
      return render_templates (home.html)

@app.route("/home")
def home ():
    return render_templates(home.html)
#_______________somme pdf_______________#
def produre_pdf_data():
    return "hello here me <h2>fatiah</h2>"
@app.route("/some")
def some ():
    pdf_data = produre_pdf_data()
    res= make_response(pdf_data)
    res.headers["content-type"] ="application/pdf"
    return res
#_______________name_______________#
@app.route("/<name>")
def hello_name (name):
    return f"<h1>hello {name}<h1>"
#_______________image_______________#
@app.route("/image")
def image ():
    return "<img href='images/4.png' alt=erreur image> "




