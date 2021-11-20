from website import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    note=db.Column(db.String(1000000))
    date=db.Column(db.DateTime(timezone=True), default=func.now())
    user_id=db.Column(db.Integer,db.ForeignKey('user.id')) #One to many relationship when one user has more than one note. One user is connected to more than one note. So one to many relationship.

class User(db.Model,UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(150),unique=True)
    password=db.Column(db.String(20))
    firstName=db.Column(db.String(150))
    notes=db.relationship('Note') #SQLALCHEMY will add the note's ID to this 'notes' column. It is a list and it will store all of the different notes. 
