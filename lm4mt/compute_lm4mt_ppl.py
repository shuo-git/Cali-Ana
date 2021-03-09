import argparse
import numpy as np
import sys
from utils import *


with open(sys.argv[1], 'r') as fr:
    lines = fr.readlines()
with open(sys.argv[2], 'r') as fr:
    src_lines = fr.readlines()

lines = [l.split() for l in lines]
src_lengths = [len(l.split()) for l in src_lines]
lines = [l[i+2:] for l, i in zip(lines, src_lengths)]

lines = [[float(x) for x in l] for l in lines]

count = sum([len(l) for l in lines])

log_prob = sum([sum(l) for l in lines])

ppl = np.exp(-log_prob / count)

print("Count = {}".format(count))
print("PPL = {:.2f}".format(ppl))
