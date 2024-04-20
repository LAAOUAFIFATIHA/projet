from flask import Flask, render_template
from flask_sqlalchemy  import SQLAlchemy


app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

somme1 = 100
listy = ["fatiha","nadia","naoual","hafssa"]


#_____________greeting_______________#


@app.route("/greeting")
def greeting ():
    return render_template ('greeting.html')
#___________somme_________________#

def somme (a,b):
        som = a+b
        return (som)

#_____________class_______________#

class etudiant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom= db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.integer(3), nullable=False)
fatiha = 
#___________homme_________________#

@app.route("/home <int:a> <int:b>")
def home (a,b):
    som = somme(a,b)
    return render_template('home.html',so = somme1, li = listy,som = som)







