from flask import Flask

import persistence
import blueprints.pages
import blueprints.entries
import blueprints.comments
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    persistence.init_app(app)

    app.register_blueprint(blueprints.pages.bp, url_prefix='/')
    app.register_blueprint(blueprints.entries.bp, url_prefix='/entries')
    # app.register_blueprint(blueprints.comments.bp, url_prefix='/comments')

    return app


if __name__ == '__main__':
    create_app().run()
