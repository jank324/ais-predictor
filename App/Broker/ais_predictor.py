import broker
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('predictor_ui.html')

@app.route('/broker/<int:file_path>')
def broker_dummy(file_path):
    return "%s" % (broker.extract_data(file_path))

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')