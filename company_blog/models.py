# since db is initialized in init file. it can be imported. 
  
from company_blog import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    profile_pic = db.Column(db.String(64), nullable = False, default='default_prof_pic.png')
    password_hash = db.Column(db.String(128))
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    
    posts = db.relationship('BlogPost', backref = 'author', lazy = False)

    def __init__(self, username, email, password) -> None:
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)
    

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


    def __repr__(self) -> str:
        return f"User is {self.username}"


class BlogPost(db.Model):

    __tablename__ = 'blogposts'

    id = db.Column(db.Integer, primary_key=True)

    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(150), nullable=False )
    text = db.Column(db.Text, nullable=False)    

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, user_id, title, text) -> None:
        self.title = title
        self.user_id = user_id
        self.text = text
    
    
    def __repr__(self) -> str:
        return f"POST ID: {self.id} -- Date: {self.date} -- Title:{self.date}"




    

    


# finally we need to prvode this the ability to have a login manager for user model
# have to set up login manager in init file 