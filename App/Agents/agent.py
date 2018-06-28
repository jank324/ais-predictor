from flask import Flask
import pickle
import sys

app = Flask(__name__)

port = int(sys.argv[1])
path = sys.argv[2]

# Figure out what you are 007!
config_file = open('%s/config.txt' % (path), 'r')
mode_string = config_file.readline()
leave_lat = float(config_file.readline())
leave_lon = float(config_file.readline())

# Load models
model_position = pickle.load(open('%s/model_position.pkl' % (path), 'rb'))
model_time = pickle.load(open('%s/model_time.pkl' % (path), 'rb'))

@app.route('/predict/<float:lat>-<float:lon>')
def predict_position(lat, lon):
    predicted_coordinate = model_position.predict([[lat, lon]])[0]
    predicted_time = model_time.predict([[lat, lon]])[0]

    if 'latitude' in mode_string:
        return ('{\"latitude\":%f, \"longitude\":%f, \"time\":%f}' % (predicted_coordinate, leave_lon, predicted_time))
    elif 'longitude' in mode_string:
        return ('{\"latitude\":%f, \"longitude\":%f, \"time\":%f}' % (leave_lat, predicted_coordinate, predicted_time))
    elif 'none' in mode_string:
        return ('{\"latitude\":%f, \"longitude\":%f, \"time\":%f}' % (leave_lat, leave_lon, predicted_time))   # TODO: Error when 'none' and either of leave_lat and leave_lon has no value
    else:
        return ('{\"error\":%s}' % (mode_string))

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=port, debug=True)