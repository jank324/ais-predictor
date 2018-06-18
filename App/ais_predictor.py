from flask import Flask
app = Flask(__name__)

@app.route('/')
def main_page():
    return "The best AIS predictor the world has ever seen!"

if __name__ == '__main__':
    app.run(debug = True)