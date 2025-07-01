from . import create_app
from .routes import home

app = create_app()
app.register_blueprint(home, url_prefix="/")