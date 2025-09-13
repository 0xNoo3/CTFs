# stolen from https://flask.palletsprojects.com/en/stable/patterns/fileuploads/

from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from pathlib import Path

import random

from kitten_detector import is_kitten

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'png'}

responses = [
    "try again"
]

app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 200 * 1024

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            if is_kitten(file.stream, eps=0.5):
                return r"ping{FlagGoesHere}"
            else:
                return random.choice(responses)
    return '''
    <!doctype html>
    <title>CatDetector</title>
    <h1>Send cats</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)