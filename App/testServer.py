from flask import Flask, request, render_template
import subprocess
import sys
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('test.html')

@app.route('/', methods=['POST'])
def my_form_post():
    f = request.files['file']
    f.save(secure_filename(f.filename))
    text = './testBroker.py'
    output = subprocess.check_output([sys.executable, text, f.filename])
    return render_template("test.html",output = output)

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')