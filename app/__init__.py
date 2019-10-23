from flask import flask
from flask_bootstrap import flask_bootstrap
from config import config_options


bootstrap = Bootstrap()

def create_app(config_name):
    '''
    Function that takes configuration setting key as an argument

    Args:
        config_name: name of the configuration to be used
    '''
    # Initializing application
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    
    # Initializing flask extensions
    bootstrap.init_app(app)

    # Registering the main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app