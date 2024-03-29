import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello123'
#######################################
########## DATABASE SETUP #############
#######################################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'blog.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# db.init_app(app)
Migrate(app,db)
app.app_context().push()


#######################################
########## LOGIN CONFIG SETUP   #######
#######################################

login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'

#######################################
########## BLUPRINT REGISTRATION ######
#######################################

from company_blog.core.views import core
from company_blog.users.views import users
from company_blog.error_pages.handlers import error_pages
from company_blog.blog_posts.views import blog_posts

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(blog_posts)
app.register_blueprint(error_pages)