import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

import cartopy.crs as ccrs
import cartopy.feature as cfeat
import cartopy.io.img_tiles as cimgt


# Constants for different places we define
Hamburg = {'Latitude': 53.55, 'Longitude': 9.81}
Rotterdam = {'Latitude': 51.9225, 'Longitude': 4.47917}
VorRott = {'Latitude': 52.43, 'Longitude': 3.43}
Ecke = {'Latitude': 53.43, 'Longitude': 4.77}
VorElbe = {'Latitude': 53.99, 'Longitude': 8.17}
InElbe ={'Latitude' :53.86, 'Longitude' : 9.29}

dis1 = 142.9 #vorRott bis Ecke
dis2 = 232.2 #ecke bis vorElbe
dis3 = 75.4 #vorElbe bis InElbe
dis4 = 48.1  #InElbe bis Hamburg

#distanz abgesteckte Strecke
def dist_to_end(obj) :
    if obj.Latitude < 52.43 :
        return vincenty(obj.Cur_Pos, (52.43, 3.43)).km + dis1 + dis2 + dis3 +dis4
    elif obj.Longitude < 4.77 :
        return vincenty(obj.Cur_Pos, (53.43, 4.77)).km + dis2 + dis3 +dis4
    elif obj.Longitude < 8.17 :
        return vincenty(obj.Cur_Pos, (53.99, 8.17)).km +dis3 + dis4
    elif obj.Longitude < 9.81 :
        return vincenty(obj.Cur_Pos, (53.55, 9.81)).km

# Plot a Google Maps map
def plot_google_map(extent, size = (13, 13)) :
    plt.figure(figsize = size)
    
    img = cimgt.GoogleTiles()

    ax = plt.axes(projection = img.crs)
    ax.set_extent(extent)
    
    ax.add_image(img, 9, interpolation = 'bicubic')     # should be 7


# Plot an OpenStreetMap map
def plot_osm_map(extent, size = (13, 13)) :
    plt.figure(figsize = size)
    
    img = cimgt.OSM()

    ax = plt.axes(projection = img.crs)
    ax.set_extent(extent)
    
    ax.add_image(img, 7, interpolation = 'bicubic')


def plot_carto_map(extent, size = (13, 13)) :
    plt.figure(figsize = size)
    
    ax = plt.axes(projection = ccrs.Mercator())
    ax.set_extent(extent)
    
    ax.add_feature(cfeat.LAND.with_scale('50m'))
    ax.add_feature(cfeat.OCEAN.with_scale('50m'))
    ax.add_feature(cfeat.COASTLINE.with_scale('50m'))
    ax.add_feature(cfeat.BORDERS.with_scale('50m'))
    ax.add_feature(cfeat.RIVERS.with_scale('50m'))
    
    # Draw Rotterdam marker
    ax.scatter(x = 4.47917, y = 51.9225, transform = ccrs.PlateCarree(), marker = '*', c = 'C1', s = 500)
    # Draw Hamburg marker
    ax.scatter(x = 10.01534, y = 53.57532, transform = ccrs.PlateCarree(), marker = '*', c = 'C1', s = 500)


# Draws a scatter plot of points to a map
def plot_to_map(size, longitude, latitude) :
    min_long = longitude.min() - 0.5
    max_long = longitude.max() + 0.5
    min_lat = latitude.min() - 0.5
    max_lat = latitude.max() + 0.5
    
    plot_carto_map((min_long, max_long, min_lat, max_lat), size = size)
    
    plt.scatter(x = longitude, y = latitude , transform = ccrs.PlateCarree(), s = 1)


def plot_trips(data, colour_col = None) :
    copy = data.loc[:, ('TripID', 'time', 'Latitude', 'Longitude', colour_col)]
    copy.set_index(['TripID', 'time'], inplace = True)

    min_lat = copy['Latitude'].min() - 0.5
    max_lat = copy['Latitude'].max() + 0.5
    min_long = copy['Longitude'].min() - 0.5
    max_long = copy['Longitude'].max() + 0.5

    plot_carto_map((min_long, max_long, min_lat, max_lat), size = (13, 13))

    for trip_id in copy.index.get_level_values(0).unique().sort_values() :
        trip_data = copy.loc[trip_id, :]
        plt.plot(x = trip_data['Longitude'], y = trip_data['Latitude'], color = trip_data[colour_col], cmap = 'autumn', transform =     ccrs.PlateCarree())


# Creates a scatter plot with colour being another dimension
def col_plot_to_map(size, longitude, latitude, col) :
    min_long = longitude.min() - 0.5
    max_long = longitude.max() + 0.5
    min_lat = latitude.min() - 0.5
    max_lat = latitude.max() + 0.5
    
    plot_carto_map((min_long, max_long, min_lat, max_lat), size = size)
    
    plt.scatter(x = longitude, y = latitude, c = col , cmap = 'autumn', transform = ccrs.PlateCarree(), s = 1)
    plt.colorbar()


from geopy.distance import vincenty
def pandasVincenty(row) :
    return vincenty(row.Cur_Pos, row.End_Pos).km 


from math import sin, cos, sqrt, atan2, radians
def dist(a_lat, a_long, b_lat, b_long) :
    R = 6373.0
    
    lat1 = radians(a_lat)
    lon1 = radians(a_long)
    lat2 = radians(b_lat)
    lon2 = radians(b_long)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance

def dist_replace_vincenty(row) :
    R = 6373.0
    
    lat1 = radians(row.Latitude)
    lon1 = radians(row.Longitude)
    lat2 = radians(row.EndLatitude)
    lon2 = radians(row.EndLongitude)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance
