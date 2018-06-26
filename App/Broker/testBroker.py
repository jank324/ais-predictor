import sys
import numpy as np
import pandas as pd

learners = ['Latitude', 'Longitude']

def extract_data(file_path):

    names = ['TripID', 'MMSI', 'StartLatitude', 'StartLongitude', 'StartTime', 'EndLatitude', 'EndLongitude', 'EndTime',
         'StartPort', 'EndPort', 'ID', 'time', 'shiptype', 'Length', 'Breadth', 'Draught', 'Latitude', 'Longitude',
         'SOG', 'COG', 'TH', 'Destination', 'Name', 'Callsign', 'AisSourcen']
    df = pd.read_csv(file_path, names = names, skiprows = 27, parse_dates = True,
                 na_values = ['?'], dtype = {'TripID': str, 'MMSI': str, 'shiptype': str})

    df['time'] = pd.to_datetime(df['time'], format = '\'%Y-%m-%d %H:%M\'')

    df.loc[df['TH'] >= 360, 'TH'] = np.nan
    df.loc[df['COG'] >= 360, 'COG'] = np.nan
    df.loc[(df['Length'] <= 0) | (df['Length'] > 400), 'Length'] = np.nan
    df.loc[(df['Breadth'] <= 0) | (df['Breadth'] > 59), 'Breadth'] = np.nan
    df.loc[df['SOG'] > 25.6, 'SOG'] = np.nan

    df = df.sort_values('time')
    coords = df[['Latitude', 'Longitude']]
    
    latlon = []
    for _, row in coords.iterrows():

        la = row['Latitude']
        lo = row['Longitude']
        lalo = [[lo, la]]
        latlon += lalo
    
    return latlon


def main(arg):
    return (extract_data(arg)) 

if __name__ == "__main__":
    main(sys.argv[1])



