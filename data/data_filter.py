import pandas

dataset = pandas.read_csv("PY11 rotterdam_hamburg - times to UNIX time.csv")

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

xs = dataset["Longitude"]
ys = dataset["Latitude"]

print dataset

"""
map = Basemap(projection='mill',resolution="h", llcrnrlon=2, llcrnrlat=51, urcrnrlon=11, urcrnrlat=55.5)
map.drawcoastlines()
map.drawcountries()
map.drawrivers()
map.fillcontinents(color='tan',lake_color='lightblue')
map.drawmapboundary(fill_color='lightblue')

map.scatter(xs, ys, latlong="True", marker="D", color="m")
"""

#plt.show()
