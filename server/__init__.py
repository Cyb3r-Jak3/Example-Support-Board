from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv("FLASK_SECRET", "CHANGEME")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db3.sqlite"
    db.init_app(app)
    db.create_all(app=app)
    login_manager = LoginManager()
    login_manager.login_view = "admin_login"
    login_manager.init_app(app)
    from .models import adminUser
    @login_manager.user_loader
    def load_user(user_id):
        return adminUser.get(int(user_id))

    db.create_all(app=app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)

    return app
