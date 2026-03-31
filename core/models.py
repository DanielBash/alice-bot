"""- Database initialization
-- Users table"""

# -- importing modules
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.mutable import MutableDict
import settings


db = SQLAlchemy()


# -- users table
class User(db.Model):
    __tablename__ = "users"
    
    # - hidden data
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)