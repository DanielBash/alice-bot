""" - Decorators for flask views"""

# -- importing modules
from functools import wraps
from flask import g, abort, redirect, url_for
import settings