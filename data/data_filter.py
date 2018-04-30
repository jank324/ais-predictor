from scipy.io import arff

data, meta = arff.loadarff("TRIPID 360933 Data direkt ROT-HAM.arff")
print "Data finished loading."

tripids = data["TripID"]
longitudes = data["Longitude"]
latitudes = data["Latitude"]

filteredLong = []
filteredlat = []
l = len(tripids)
for i in range(0, l):
    if tripids[i] == 360933:
        filteredLong.append(longitudes[i])
        filteredlat.append(latitudes[i])

import matplotlib.pyplot as plt

plt.plot(filteredLong, filteredlat, "ro")
plt.axis([2.89, 10.0, 51.68, 54.54])
plt.show()