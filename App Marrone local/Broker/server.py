from flask import Flask, flash, jsonify, request, render_template, session
import broker
import os

ON_HEROKU = os.environ.get('ON_HEROKU')
if ON_HEROKU:
    port = int(os.environ.get('PORT', 17995))
else:
    port = 80

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def show_main_page():
    return render_template('main_page.html')

@app.route('/trip', methods=['POST'])
def upload_trip():
    file = request.files['tripfile']
    return broker.load_learners(file)

@app.route('/prediction', methods=['POST'])
def make_prediction():
    origin_point = request.json
    route, time = broker.predict(origin_point)
    info = {'time': time, 'route': route}
    return jsonify(info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)