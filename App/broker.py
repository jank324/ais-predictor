# Gets trip lines (arff)
# Take out values I care about (learned on)
# while current position isn't destination
#     Determine agent for current position
#     Send values to agent
#     Receive new values at sector leave from agent (e.g. leave latitude, leave longitude, time to leave)
#     Add sector travel time to entire travel time
# return entire travel time and route

import numpy as np
import pandas as pd
import sys

file_path = sys.argv[1]
print('The file path is \"%s\"' % (file_path))

# Load the data
names = ['TripID', 'MMSI', 'StartLatitude', 'StartLongitude', 'StartTime', 'EndLatitude', 'EndLongitude', 'EndTime',
         'StartPort', 'EndPort', 'ID', 'time', 'shiptype', 'Length', 'Breadth', 'Draught', 'Latitude', 'Longitude',
         'SOG', 'COG', 'TH', 'Destination', 'Name', 'Callsign', 'AisSourcen']
df = pd.read_csv(file_path, names = names, skiprows = 27, parse_dates = True,
                 na_values = ['?'], dtype = {'TripID': str, 'MMSI': str, 'shiptype': str})

# Convert time columns to correct dtype
df['StartTime'] = pd.to_datetime(df['StartTime'], format = '\'%Y-%m-%d %H:%M\'')
df['EndTime'] = pd.to_datetime(df['EndTime'], format = '\'%Y-%m-%d %H:%M\'')
df['time'] = pd.to_datetime(df['time'], format = '\'%Y-%m-%d %H:%M\'')

# Convert all headings that are 511 (>= 360) to NaN
df.loc[df['TH'] >= 360, 'TH'] = np.nan

# Convert courses >= 360 to NaN
df.loc[df['COG'] >= 360, 'COG'] = np.nan

# Set invalid shiptypes to NaN
# Invalid shiptypes existing in the data set are '0' and '159'
df.loc[(df['shiptype'] == '0') | (df['shiptype'] == '159'), 'shiptype'] = np.nan

# Set invalid lengths (0 or > 400) to NaN
df.loc[(df['Length'] <= 0) | (df['Length'] > 400), 'Length'] = np.nan

# Set invalid breadths (0 or > 59) to NaN
df.loc[(df['Breadth'] <= 0) | (df['Breadth'] > 59), 'Breadth'] = np.nan

# Set speeds that are unrealisticly high to NaN
df.loc[df['SOG'] > 25.6, 'SOG'] = np.nan

df = df.drop(['AisSourcen', 'ID', 'StartPort', 'EndPort', 'Name', 'MMSI', 'shiptype'], axis = 1)

print(df)