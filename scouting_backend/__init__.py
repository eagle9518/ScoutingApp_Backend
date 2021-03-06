from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os, sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        from .home import home
        from .retrieval import retrieval
        from .analysis import analysis
        from .api import api
        from .google import google
        from .pit import pit

        app.register_blueprint(home.home_bp)
        app.register_blueprint(retrieval.retrieval_bp, url_prefix="/retrieval")
        app.register_blueprint(analysis.analysis_bp, url_prefix="/analysis")
        app.register_blueprint(api.api_bp, url_prefix="/api")
        app.register_blueprint(google.google_bp, url_prefix="/google")
        app.register_blueprint(pit.pit_bp, url_prefix="/pit")

        # Make sure that table no longer exists if you want to update columns
        # db.create_all()

        return app
