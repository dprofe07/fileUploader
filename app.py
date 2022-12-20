import os
import sys

from flask import Flask, render_template, redirect, flash, request, url_for
from werkzeug.utils import secure_filename

is_server = os.path.exists('/SERVER/is_server')

app = Flask(__name__)
app.secret_key = "daghfdgmkfhjdfgsnasfasfa"

if len(sys.argv) >= 2 and sys.argv[1] != '':
    app.upload_folder = sys.argv[1]
elif is_server:
    app.upload_folder = '/SERVER/share'
else:
    app.upload_folder = './uploaded/'

if is_server:
    prefix = '/file-uploader'
else:
    prefix = ''


@app.route(prefix + '/')
def index():
    return render_template('index.html')


@app.route(prefix + '/loaded', methods=['POST'])
def page_loaded():
    file = request.files['file']

    if not file:
        flash('Error. Try again', 'color: red;')
    else:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.upload_folder, filename))
        flash('Success', 'color: green;')
    return redirect(url_for('page_index'))


if __name__ == '__main__':
    if is_server:
        app.run('127.0.0.1', port=8004)
    else:
        app.run('0.0.0.0', port=5000)
