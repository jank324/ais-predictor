import sys
from PIL import Image
import numpy as np
import os
import pandas as pd

#learners = ['Latitude', 'Longitude']

#def extract_data(file_path):

#    names = ['TripID', 'MMSI', 'StartLatitude', 'StartLongitude', 'StartTime', 'EndLatitude', 'EndLongitude', 'EndTime',
#         'StartPort', 'EndPort', 'ID', 'time', 'shiptype', 'Length', 'Breadth', 'Draught', 'Latitude', 'Longitude',
#         'SOG', 'COG', 'TH', 'Destination', 'Name', 'Callsign', 'AisSourcen']
#    df = pd.read_csv(file_path, names = names, skiprows = 27, parse_dates = True,
#                 na_values = ['?'], dtype = {'TripID': str, 'MMSI': str, 'shiptype': str})

#    df['time'] = pd.to_datetime(df['time'], format = '\'%Y-%m-%d %H:%M\'')

#    df.loc[df['TH'] >= 360, 'TH'] = np.nan
#    df.loc[df['COG'] >= 360, 'COG'] = np.nan
#    df.loc[(df['Length'] <= 0) | (df['Length'] > 400), 'Length'] = np.nan
#    df.loc[(df['Breadth'] <= 0) | (df['Breadth'] > 59), 'Breadth'] = np.nan
#    df.loc[df['SOG'] > 25.6, 'SOG'] = np.nan

#    return df[learners]


def main(arg):
    img  = Image.open(arg)
    width, height = img.size
    print(width)

if __name__ == "__main__":
    main(sys.argv[1])