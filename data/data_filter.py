from scipy.io import arff

data, meta = arff.loadarff("PY09 rotterdam_hamburg - Dates Numeric.arff")
print "Data finished loading."

print data["time"][0:10]

times = data["time"]
for i in range(0, len(times)):
    t = times[i]
    times[i] = t / 1000
data["time"] = times

start_times = data["StartTime"]
for i in range(0, len(start_times)):
    t = start_times[i]
    start_times[i] = t / 1000
data["StartTime"] = start_times

end_times = data["EndTime"]
for i in range(0, len(end_times)):
    t = end_times[i]
    end_times[i] = t / 1000
data["EndTime"] = end_times

print "---------------------------------------------"
print data["time"][0:10]

#tripids = data["TripID"]
#longitudes = data["Longitude"]
#latitudes = data["Latitude"]

#import matplotlib.pyplot as plt
#
#plt.plot(longitudes, latitudes, "ro")
#plt.axis([2.89, 10.0, 51.68, 54.54])
#plt.show()