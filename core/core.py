"""- Core functions, and overall app logic"""

# -- importing modules
from werkzeug.security import generate_password_hash, check_password_hash
import settings
from core.logger import log
import docker


def create_app(name):
    from .flask_shortcuts import initialize_app
    return initialize_app.create_app(name)