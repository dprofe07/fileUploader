import os
import sys

from flask import Flask, render_template, redirect, flash, request
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "daghfdgmkfhjdfgsnasfasfa"
if len(sys.argv) < 2 or sys.argv[1] == '':
    app.upload_folder = './uploaded/'
else:
    app.upload_folder = sys.argv[1]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/loaded', methods=['POST'])
def got():
    file = request.files['file']

    if not file:
        flash('Error. Try again', 'color: red;')
    else:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.upload_folder, filename))
        flash('Success', 'color: green;')
    return redirect('/')


if __name__ == '__main__':
    app.run('0.0.0.0', port=8004)
