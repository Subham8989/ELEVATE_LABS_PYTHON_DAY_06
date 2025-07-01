from flask import Flask
from ..config import Config

def create_app():
  app = Flask(__name__, template_folder="views", static_folder="assets")
  app.config.from_object(Config)
  return app