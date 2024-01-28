# essentially views files for error pages. 

from flask import Blueprint, render_template

error_pages = Blueprint('error_pages', __name__)

@error_pages.app_errorhandler(404)
def error_404(error):

    return render_template('error_pages/404.html'), 404


@error_pages.app_errorhandler(403)
def error_403(error):
    return render_template('error_pages/403.html'), 403


# since this isnt just basic routing, 
# app_errorhandler is used to connect to a general error