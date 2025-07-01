from flask import Blueprint, render_template

home = Blueprint("home", __name__)

@home.route("/")
@home.route("/home")
def home_():
  return render_template("index.html"), 200