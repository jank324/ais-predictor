from flask import Flask
import pickle
import sys

app = Flask(__name__)

# Figure out what you are 007!
config_file = open('config.txt', 'r')
mode_string = config_file.readline()
leave_lat = float(config_file.readline())
leave_lon = float(config_file.readline())

# Load models
model_position = pickle.load(open('model_position.pkl', 'rb'))
model_cog = pickle.load(open('model_cog.pkl', 'rb'))
model_sog = pickle.load(open('model_sog.pkl', 'rb'))
model_time = pickle.load(open('model_time.pkl', 'rb'))

@app.route('/predict/<float:lat>-<float:lon>-<float:cog>-<float:sog>')
def predict_position(lat, lon, cog, sog):
    predicted_coordinate = model_position.predict([[lat, lon, cog, sog]])[0]
    predicted_cog = model_cog.predict([[lat, lon, cog, sog]])[0]
    predicted_sog = model_sog.predict([[lat, lon, cog, sog]])[0]
    predicted_time = model_time.predict([[lat, lon, cog, sog]])[0]

    if 'latitude' in mode_string:
        return ('{\"latitude\":%f, \"longitude\":%f, \"cog\":%f, \"sog\":%f, \"time\":%f}' % (predicted_coordinate,
                                                                                              leave_lon,
                                                                                              predicted_cog,
                                                                                              predicted_sog,
                                                                                              predicted_time))
    elif 'longitude' in mode_string:
        return ('{\"latitude\":%f, \"longitude\":%f, \"cog\":%f, \"sog\":%f, \"time\":%f}' % (leave_lat,
                                                                                              predicted_coordinate,
                                                                                              predicted_cog,
                                                                                              predicted_sog,
                                                                                              predicted_time))
    elif 'none' in mode_string:
        return ('{\"latitude\":%f, \"longitude\":%f, \"cog\":%f, \"sog\":%f, \"time\":%f}' % (leave_lat,
                                                                                              leave_lon,
                                                                                              predicted_cog,
                                                                                              predicted_sog,
                                                                                              predicted_time))   # TODO: Error when 'none' and either of leave_lat and leave_lon has no value
    else:
        return ('{\"error\":%s}' % (mode_string))

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5000, debug=True)