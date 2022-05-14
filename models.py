from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

# creates a db instance
db = SQLAlchemy()

# connects to db
def connect_db(app):
    db.app = app
    db.init_app(app)
