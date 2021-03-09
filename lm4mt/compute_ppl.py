import argparse
import numpy as np
import sys
from utils import *


with open(sys.argv[1], 'r') as fr:
    lines = fr.readlines()

lines = [[float(x) for x in l.split()] for l in lines]

count = sum([len(l) for l in lines])

log_prob = sum([sum(l) for l in lines])

ppl = np.exp(-log_prob / count)

print(ppl)
