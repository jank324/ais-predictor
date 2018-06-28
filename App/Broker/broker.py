import numpy as np
import pandas as pd
import requests

learners = ['latitude', 'longitude']

routes = {
    'rot_ham': {
        0: {
            'area': {'min_lat': None, 'max_lat': 52.8, 'min_lon': None, 'max_lon': 4.8},
            'agent_url': '192.168.178.32:5300'},
        1: {
            'area': {'min_lat': 52.8, 'max_lat': None, 'min_lon': None, 'max_lon': 4.8},
            'agent_url': '192.168.178.32:5301'},
        2: {
            'area': {'min_lat': None, 'max_lat': None, 'min_lon': 4.8, 'max_lon': 6.0},
            'agent_url': '192.168.178.32:5302'},
        3: {
            'area': {'min_lat': None, 'max_lat': None, 'min_lon': 6.0, 'max_lon': 7.2},
            'agent_url': '192.168.178.32:5303'},
        4: {
            'area': {'min_lat': None, 'max_lat': None, 'min_lon': 7.2, 'max_lon': 8.6},
            'agent_url': '192.168.178.32:5304'},
        5: {
            'area': {'min_lat': None, 'max_lat': None, 'min_lon': 8.6, 'max_lon': 9.81},
            'agent_url': '192.168.178.32:5305'}
    }
}

def load_learners(file):
    names = ['trip', 'mmsi', 'start_latitude', 'start_longitude', 'start_time', 'end_latitude', 'end_longitude', 'end_time',
             'start_port', 'end_port', 'id', 'time', 'shiptype', 'length', 'breadth', 'draught', 'latitude', 'longitude',
             'sog', 'cog', 'th', 'destination', 'name', 'callsign', 'ais_sourcen']
    df = pd.read_csv(file, names=names, skiprows=27, parse_dates=True, na_values=['?'], dtype={'trip': str, 'mmsi': str, 'shiptype': str})

    df['time'] = pd.to_datetime(df['time'], format='\'%Y-%m-%d %H:%M\'')

    df.loc[df['th'] >= 360, 'th'] = np.nan
    df.loc[df['cog'] >= 360, 'cog'] = np.nan
    df.loc[(df['length'] <= 0) | (df['length'] > 400), 'length'] = np.nan
    df.loc[(df['breadth'] <= 0) | (df['breadth'] > 59), 'breadth'] = np.nan
    df.loc[df['sog'] > 25.6, 'sog'] = np.nan

    df.loc[df['start_port'] == 'ROTTERDAM', 'start_port'] = 'ROT'
    df.loc[df['end_port'] == 'HAMBURG', 'end_port'] = 'HAM'

    df = df.sort_values('time')
    df = df[['time', 'start_port', 'end_port'] + learners]
    
    return df.to_json(orient='records')

def is_in_area(point, area):
    if area['min_lat'] != None and point['latitude'] < area['min_lat']:
        return False
    if area['max_lat'] != None and point['latitude'] > area['max_lat']:
        return False
    if area['min_lon'] != None and point['longitude'] < area['min_lon']:
        return False
    if area['max_lon'] != None and point['longitude'] > area['max_lon']:
        return False
    return True

def predict(origin_point):
    route = routes['rot_ham']

    predicted_route = [{'latitude': origin_point['latitude'], 'longitude': origin_point['longitude']}]
    predicted_time = 0

    for sector in route:
        if is_in_area(point=predicted_route[-1], area=route[sector]['area']):
            url = route[sector]['agent_url']
            response = requests.get('http://%s/predict/%f-%f' % (url, predicted_route[-1]['latitude'], predicted_route[-1]['longitude'])).json()

            predicted_route.append({'latitude': response['latitude'], 'longitude': response['longitude']})
            predicted_time += response['time']

    return predicted_route, predicted_time