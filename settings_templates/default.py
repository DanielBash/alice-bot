"""- Default settings template"""

# -- importing modules
from pathlib import Path

# -- flask settings
PORT = 8080  # running port
HOST = '0.0.0.0'  # on what host to run app
SECRET_KEY = 'unsecure-secret-key'  # app secret key for cryptography. sessions, for example

# -- app settings
DEBUG = False  # is app run in debug mode?
PRINT_CONSTANTS = True  # do we need to print settings when initializing?

# -- sqlalchemy database settings
SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'  # database connection uri
TEMPLATE_PATH = Path('templates')  # templates folder path

# -- blueprints settings
BASE_BLUEPRINTS = ['main', 'index']  # blueprints that can be handled without url prefix
