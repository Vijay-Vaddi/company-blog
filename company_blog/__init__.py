from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
app = Flask(__name__)

#######################################
########## DATABASE SETUP #############
#######################################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'blog.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)
app.app_context().push()
Migrate(app,db)

#######################################
########## BLUPRINT REGISTRATION ######
#######################################


from company_blog.core.views import core
from company_blog.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(error_pages)