import sys
import numpy as np


for line in sys.stdin:
    print('{:.2f}'.format(np.sum([float(x) for x in line.split()])))
