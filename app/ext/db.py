from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
  app.Database = db.init_app(app)