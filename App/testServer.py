from flask import Flask, request, render_template
import subprocess
import sys
from werkzeug.utils import secure_filename
import os

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def my_form():
    return render_template('test.html')

@app.route('/', methods=['GET', 'POST'])
def my_form_post():
    f = request.files['file']
    name = './static/'
    name += f.filename
    f.save(name)
    text = './testBroker.py'
    subprocess.check_output([sys.executable, text, name])
    #file_name = os.path.join(pictures, f.filename)
    output = './static/pic.jpg'
    return render_template("test.html", output = output)

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')