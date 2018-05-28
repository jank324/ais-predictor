import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

import cartopy.crs as ccrs
import cartopy.feature as cfeat
import cartopy.io.img_tiles as cimgt


# Constants for different places we define
pos_ham = {'Latitude': 53.55, 'Longitude': 9.81}
pos_rot = {'Latitude': 51.92, 'Longitude': 4.48}
pos_off_rot = {'Latitude': 52.43, 'Longitude': 3.43}
pos_rot_ham_corner = {'Latitude': 53.43, 'Longitude': 4.77}
pos_off_elb = {'Latitude': 53.99, 'Longitude': 8.17}
pos_in_elb = {'Latitude' : 53.86, 'Longitude': 9.29}


# ----- FUNKTIONEN ZUM PLOTTEN -----


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


# ----- FUNKTIONEN ZUR DISTANZBERECHNUNG -----


from math import sin, cos, sqrt, atan2, radians


# Bee line distance of two positions
def beeline_dist(a_lat, a_long, b_lat, b_long) :
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


# Distance to Hamburg along beaconed route (ROT-HAM)
def route_dist_to_ham(lat, long) :
    dist_1 = 142.9 # pos_off_rot to pos_rot_ham_corner
    dist_2 = 232.2 # pos_rot_ham_corner to pos_off_elb
    dist_3 = 75.4  # pos_off_elb to pos_in_elb
    dist_4 = 48.1  # pos_in_elb to pos_ham

    if lat < 52.43 :
        return beeline_dist(lat, long, pos_off_rot['Latitude'], pos_off_rot['Longitude']) + dist_1 + dist_2 + dist_3 + dist_4
    elif long < 4.77 :
        return beeline_dist(lat, long, pos_rot_ham_corner['Latitude'], pos_rot_ham_corner['Longitude']) + dist_2 + dist_3 + dist_4
    elif long < 8.17 :
        return beeline_dist(lat, long, pos_off_elb['Latitude'], pos_off_elb['Longitude']) + dist_3 + dist_4
    elif long < 9.81 :
        return beeline_dist(lat, long, pos_ham['Latitude'], pos_ham['Longitude'])
