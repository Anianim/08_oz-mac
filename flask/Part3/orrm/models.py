# Model -> Table 생성
# 게시글 - board
# 유저 - user

from db import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False) 
    adress = db.Column(db.String(120), nullable=False) 
    boards = db.relationship('Board', back_populates='author', lazy='dynamic') 
    # lazy = dynamic 특정 글만 조회 할 수 있음.
    

class Board(db.Model):
    __tablename__ = "boards"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(300)) 
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    author = db.relationship('User', back_populates='boards')