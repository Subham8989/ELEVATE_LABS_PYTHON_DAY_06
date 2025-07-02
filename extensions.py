from flask_sqlalchemy import SQLAlchemy
from flask_hcaptcha import hCaptcha

db = SQLAlchemy()
hcaptcha = hCaptcha()