import pandas

dataset = pandas.read_csv("PY10 rotterdam_hamburg.csv")

dataset["StartTime"] = dataset["StartTime"] / 1000
dataset["EndTime"] = dataset["EndTime"] / 1000
dataset["time"] = dataset["time"] / 1000

dataset.to_csv("PY11 rotterdam_hamburg - times to UNIX time.csv")