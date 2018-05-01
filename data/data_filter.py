import pandas
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeat

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(1, 1, 1, projection = ccrs.EuroPP())

ax.coastlines(resolution='10m')
#ax.background_img(resolution="high")

ax.set_extent([2,11,51,55.5])
#rivers_and_lakes = cfeat.NaturalEarthFeature(category="cultural", name ="admin_0_boundary_lines", scale ="10m", facecolor= "none")
#ax.add_feature(rivers_and_lakes, linestyle =":", edgecolor ="blue")



'''map = Basemap(projection='mill',resolution="h", llcrnrlon=2, llcrnrlat=51, urcrnrlon=11, urcrnrlat=55.5)
map.drawcoastlines()
map.drawcountries()
map.drawrivers()
map.fillcontinents(color='tan',lake_color='lightblue')
map.drawmapboundary(fill_color='lightblue')
'''
dataset = pandas.read_csv("PY12 rot-ham - spalten bereinigt.csv")

xs = dataset["Longitude"]
ys = dataset["Latitude"]
plt.scatter(xs, ys, s=1, c="red", alpha=0.5,transform=ccrs.Geodetic())
plt.show()
