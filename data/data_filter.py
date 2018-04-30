from scipy.io import arff
import pandas

raw_data = arff.loadarff("PY09 rotterdam_hamburg - Dates Numeric.arff")
print "Data finished loading."

dataset = pandas.DataFrame(raw_data[0])

dataset.to_csv("rot-ham_pandas_test.csv")