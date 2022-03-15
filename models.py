from datetime import datetime
import os
from sqlalchemy import Column, String, Integer, create_engine, ForeignKey
from flask_sqlalchemy import SQLAlchemy
import json
from config import DatabaseURI

# Creating DB
database_path = DatabaseURI.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()



# Movies Model
class Movie(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)
    image = Column(String)
    release_date = Column(db.DateTime)
    actors = db.relationship('Actor', backref='Movie',
                                lazy='dynamic')

    def __init__(self, title, image, release_date):
        self.title = title
        self.image = image
        self.release_date = release_date

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def format(self):
        return {
        'id': self.id,
        'title': self.title,
        'image': self.image,
        'release_date': self.release_date
        }
    

# Actors Model
class Actor(db.Model):
    ___tablename___ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    age = Column(Integer)
    gender = Column(String)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))

    def __init__(self, name, age, gender, movie_id):
        self.name = name
        self.age = age
        self.gender = gender
        self.movie_id = movie_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def format(self):
        return {
        'id': self.id,
        'name': self.name,
        'age': self.age,
        'gender': self.gender,
        'movie_id': self.movie_id
        }
 

 
    