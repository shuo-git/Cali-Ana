import sys
import numpy as np


for line in sys.stdin:
    print('{:.2f}'.format(np.mean([float(x) for x in line.split()])))

# for line in sys.stdin:
#     print('{:.2f}'.format(np.exp(float(line.strip()))))