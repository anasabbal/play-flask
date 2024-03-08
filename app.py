from flask import Flask
from flask_migrate import Migrate

from config.config import db, set_db_configs, create_tables, configure_logging
from routes.user_api import user_controller


def create_app():
    app = Flask(__name__)
    Migrate(app, db)
    set_db_configs(app)
    configure_logging(app)
    create_tables(app)
    app.register_blueprint(user_controller)
    return app