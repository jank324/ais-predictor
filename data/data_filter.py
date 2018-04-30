import pandas

dataset = pandas.read_csv("PY11 rotterdam_hamburg - times to UNIX time.csv")

import matplotlib.pyplot as plt

xs = dataset["Longitude"]
ys = dataset["Latitude"]

plt.plot(xs, ys, "x")
plt.show()