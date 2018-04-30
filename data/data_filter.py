from scipy.io import arff

data = arff.loadarff("B13a rotterdam_hamburg - ursula teils aussortiert.arff")

print data.count