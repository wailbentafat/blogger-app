from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app.app import db
Base = declarative_base()

class user(Base):
    __tablename__ = 'posts'
    user_id=db.Column(Integer,unique=True,primary_key=True,autoincrement=True)
    username =db.Column(String(30),primary_key=True , unique=True)
    password=db.Column(String(40), nullable=False)
    user=db.relationship( 'post',backref='author')

class post(Base):
    __tablename__ = 'posts'
    content=db.Column(String(600),nullable=False)
    title=db.Column(String(40),nullable=False)
    id=db.Column(Integer,autoincrement=True,primary_key=True)
    author_id=db.relationship('base',foreign_keys=('users.id'))

  