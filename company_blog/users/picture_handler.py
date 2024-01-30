import os
from flask import current_app
from PIL import Image

def add_profile_pic(pic_upload, username):

    filename = pic_upload.filename
    extension = filename.split('.')[-1]
    saved_name = str(username)+'.'+extension
    #to keep file names unique, its saved with unique username. can hash it if we want later

    file_path = os.path.join(current_app, 'static/profile_pics', saved_name)
    # where to save

    output_size = (200, 200)

    img = Image.open(pic_upload)
    img.thumbnail(output_size)
    img.save(file_path)

    return saved_name