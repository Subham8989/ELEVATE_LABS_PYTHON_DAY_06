from flask import Blueprint, render_template

about = Blueprint("about", __name__)

@about.route('/about')
def about_():
  return render_template("about.html"), 200