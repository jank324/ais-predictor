from flask import Flask, flash, jsonify, request, render_template, session
import broker

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
    app.run(host='0.0.0.0', port=80, debug=True)