from flask import Flask

from flask_migrate import Migrate

from ..config import Config
from ..extensions import db, hcaptcha


def create_app():
  app = Flask(__name__, template_folder="views", static_folder="assets")
  app.config.from_object(Config)
  db.init_app(app)
  hcaptcha.init_app(app)
  Migrate(app, db, directory="app/migrations")
  return app