from flask import current_app
import os

def save_img(file):
    file.save(os.path.join(current_app.config['UPLOAD_FOLDER'],'img',file.filename))