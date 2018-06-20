import sys
from PIL import Image
import numpy as np
import os
import pandas as pd
sys.path.append('../data/AISMapPlot.py')
import AISMapPlot as aismap
import matplotlib.pyplot as plt

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

    aismap.plot_to_map(size = (13, 13), longitude = df['Longitude'], latitude = df['Latitude'])
    picName = './static/pic.jpg'
    plt.savefig(picName)

    return picName

def main(arg):
    return (extract_data(arg))


if __name__ == "__main__":
    main(sys.argv[1])




#img  = Image.open(arg)
#    width, height = img.size
#    print(width)
