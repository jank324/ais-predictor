from scipy.io import arff

data, meta = arff.loadarff("TRIPID 360933 Data direkt ROT-HAM.arff")
print "Data finished loading."

print data["time"][0:5]