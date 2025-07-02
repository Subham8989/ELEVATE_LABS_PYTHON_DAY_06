import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_NAME = os.getenv("DB_NAME")

class Config:
  SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_DIR, "app", "db", DB_NAME)}'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_ECHO = True
  SECRET_KEY = os.getenv("SECRET_KEY")
  HCAPTCHA_SITE_KEY = os.getenv("HCAPTCHA_SITE_KEY")
  HCAPTCHA_SECRET_KEY = os.getenv("HCAPTCHA_SECRET_KEY")