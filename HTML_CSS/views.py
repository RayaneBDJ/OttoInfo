from flask import Blueprint, render_template

views = Blueprint(__name__, "views") 

@views.route("/")
def home_page():
    return render_template('home_page.html')

@views.route("/accueil/")
def accueil():
    return render_template('accueil.html')

@views.route("/contact/")
def contact():
    return render_template("contact.html")

@views.route("/test/")
def test():
    return render_template("test.html")


@views.route("/coureurs/")
def coureurs():
    return render_template("coureurs.html")

@views.route("/ecuries/")
def ecuries():
    return render_template("ecuries.html")

@views.route("/gagnants/")
def gagnants():
    return render_template("gagnants.html")

@views.route("/circuits/")
def circuits():
    return render_template("circuits.html")