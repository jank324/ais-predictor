from flask import Flask, flash, request, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def show_main_page():
    return render_template('main_page.html')

@app.route('/uploadtrip', methods=['POST'])
def upload_trip():
    file = request.files['tripfile']
    file.save('uploads/to_predict.arff')    # TODO: Check if .arff
    return 'File saved!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)