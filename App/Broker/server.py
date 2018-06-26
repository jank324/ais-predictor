from flask import Flask, flash, request, render_template
import os
import subprocess
import sys

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def show_main_page():
    return render_template('main_page.html')

@app.route('/uploadtrip', methods=['POST'])
def upload_trip():
    file = request.files['tripfile']
    file.save('uploads/trip.arff')    # TODO: Check if .arff
    return 'File saved!'

'''@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(UPLOAD_FOLDER + f.filename)
        output = subprocess.check_output([sys.executable, './testBroker.py', name])
        return render_template("test.html",geojson = output, output2 = '')'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)