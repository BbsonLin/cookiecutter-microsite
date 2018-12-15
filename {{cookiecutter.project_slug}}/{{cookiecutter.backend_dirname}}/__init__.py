import os

from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__,
                template_folder=os.path.abspath(os.getenv('FLASK_TEMPLATE_FOLDER', 'templates')),
                static_folder=os.path.abspath(os.getenv('FLASK_STATIC_FOLDER', 'static')),
                static_url_path='')
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY='dev',
        # store the database in the instance folder
        SQLALCHEMY_DATABASE_URI='sqlite:///{}'.format(os.path.join(app.root_path, 'dev.sqlite')),
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py')
    else:
        # load the test config if passed in
        app.config.update(test_config)

    return app


app = create_app()
