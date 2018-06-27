from flask import Flask, flash, request, render_template, session
import broker

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def show_main_page():
    return render_template('main_page.html')

@app.route('/trip', methods=['POST'])
def upload_trip():
    file = request.files['tripfile']
    return broker.load_learners(file)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)