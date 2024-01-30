from flask import Flask
from datetime import datetime,time
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import TEXT
db =SQLAlchemy()





class Contact(db.Model):
    __tablename__ = 'contactus' 
    contact_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    contact_name=db.Column(db.String(100),nullable=True)
    contact_email = db.Column(db.String(100),nullable=True)
    contact_no=db.Column(db.String(100),nullable=True)
    contact_message = db.Column(db.String(100),nullable=True)