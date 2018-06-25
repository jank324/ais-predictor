from flask import Flask
import pickle
import sys

app = Flask(__name__)

path = sys.argv[1]

# Figure out what you are 007!
config_file = open('%s/config.txt' % (path), 'r')
mode_string = config_file.readline()
leave_lat = float(config_file.readline())
leave_lon = float(config_file.readline())

# Load models
model_position = pickle.load(open('%s/model_position.pkl' % (path), 'rb'))
model_time = pickle.load(open('%s/model_time.pkl' % (path), 'rb'))

@app.route('/position/<float:lat>-<float:lon>')
def predict_position(lat, lon):
    predicted = model_position.predict([[lat, lon]])[0]

    if 'latitude' in mode_string:
        return ('%f-%f' % (predicted, leave_lon))
    elif 'longitude' in mode_string:
        return ('%f-%f' % (leave_lat, predicted))
    elif 'none' in mode_string:
        return ('%f-%f' % (leave_lat, leave_lon))   # TODO: Error when 'none' and either of leave_lat and leave_lon has no value
    else:
        return ('ERROR: The agent\'s mode string is invalid: \"%s\"' % (mode_string))
    
@app.route('/time/<float:lat>-<float:lon>')
def predict_time(lat, lon):
    mins_to_leave = model_time.predict([[lat, lon]])[0]
    return ('%f' % (mins_to_leave))

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)