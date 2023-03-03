from flask import Flask
from app.api import config_blueprint
from app.database import config_database
from app import config_extensions


def create_app():
    flask_app = Flask(__name__)
    flask_app.config.from_object('config_dev')  # config config_dev config_prod
    config_extensions(flask_app)
    config_database(flask_app)
    config_blueprint(flask_app)
    return flask_app


app = create_app()

if __name__ == '__main__':
    app.run(
        app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG']
    )