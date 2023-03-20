from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base


class EntityBase(Base):
    abstract = True
    id = db.Column(db.Integer, primary_key=True)
    