import utils
import sys


for line in sys.stdin:
    scores = ['{:.2f}'.format(float(x)) for x in line.split()]
    print(' '.join(scores))
