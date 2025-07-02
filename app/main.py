from flask import render_template, send_from_directory
import os

from . import create_app
from .routes import home, about, projects, contact

PUBLIC_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "public")

app = create_app()
app.register_blueprint(home, url_prefix="/")
app.register_blueprint(about, url_prefix="/")
app.register_blueprint(projects, url_prefix="/")
app.register_blueprint(contact, url_prefix="/")

@app.errorhandler(400)
def error_400(error):
  return render_template("errors/400.html", data={ "error": error }), 400

@app.errorhandler(401)
def error_401(error):
  return render_template("errors/401.html", data={ "error": error }), 401

@app.errorhandler(403)
def error_403(error):
  return render_template("errors/403.html", data={ "error": error }), 403

@app.errorhandler(404)
def error_404(error):
  return render_template("errors/404.html", data={ "error": error }), 404

@app.errorhandler(405)
def error_405(error):
  return render_template("errors/405.html", data={ "error": error }), 405

@app.errorhandler(500)
def error_500(error):
  return render_template("errors/500.html", data={ "error": error }), 500

@app.route("/robots.txt")
def robots():
  return send_from_directory(PUBLIC_DIR, "robots.txt"), 200