from flask import Flask, request, render_template
import subprocess
import sys
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('test.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    output = subprocess.check_output([sys.executable, text, "34"])
    return output

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')