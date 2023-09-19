 
from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
from app.routes import app

UPLOAD_FOLDER = 'app/uploads'
ALLOWED_EXTENSIONS = {'csv', 'xlsx'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if __name__ == '__main__':
    app.run(debug=True)
