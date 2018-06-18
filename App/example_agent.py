# Receive learners from broker
# Run machine learning model to determine learners at sector leave
# Return learners at sector leave to broker

import sys

lon = float(sys.argv[1])
lat = float(sys.argv[2])

result = lon * lat
print('Agent: %f' % (result))