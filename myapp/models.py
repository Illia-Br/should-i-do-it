#models 
from myapp import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
#allows to set up isAuthenticate etc 
from flask_login import UserMixin
from datetime import datetime
from sqlalchemy.sql import func

#login management 
# allows us to use this in templates for isUser stuff 
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy=True)
    comments = db.relationship('Comment', backref='author', lazy=True)
    votes = db.relationship('Vote', backref='author', lazy=True)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

#going to use this in our login view 
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f"Username {self.username}"

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), nullable=False, default=func.now())
    title = db.Column(db.String(160), nullable=False)
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    comments = db.relationship('Comment', cascade = 'all,delete',backref='target', lazy=True)
    votes = db.relationship('Vote', cascade = 'all,delete',backref='target', lazy=True)

    def __init__(self, title, description, user_id):
        self.title = title
        self.description = description
        self.user_id = user_id
    
    def __repr__(self):
        return f"Post ID: {self.id} -- Date: {self.date} --- Title: {self.title}"

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), nullable=False, default=func.now())
    text = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, text, post_id, user_id):
        self.text = text
        self.post_id = post_id
        self.user_id = user_id
    
    def __repr__(self):
        return f"Comment ID: {self.id} -- Date: {self.date} --- Text: {self.text}"

class Vote(db.Model):
    __tablename__ = 'votes'
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    vote_pro = db.Column(db.Integer, default = 0)
    vote_against = db.Column(db.Integer, default = 0)

    def __init__(self, post_id, user_id, vote_pro, vote_against):
        self.post_id = post_id
        self.user_id = user_id
        self.vote_pro = vote_pro
        self.vote_against = vote_against
    
    def __repr__(self):
        return f"Comment ID: {self.id} -- Vote Pro: {self.vote_pro} --- Vote Against: {self.vote_against}"