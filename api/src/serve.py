from flask import Flask
from src import routes
from src.lib import log


def create_app():
    log.setup()
    app = Flask(__name__)
    app.register_blueprint(routes.calendar, url_prefix='/calendar')
    app.register_blueprint(routes.health, url_prefix='/health')
    app.register_blueprint(routes.messenger, url_prefix='/messenger')
    return app


if __name__ == '__main__':
    create_app()



