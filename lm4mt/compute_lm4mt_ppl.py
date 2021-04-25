import argparse
import numpy as np
import sys
from utils import *


with open(sys.argv[1], 'r') as fr:
    src_lines = fr.readlines()
with open(sys.argv[2], 'r') as fr:
    lines = fr.readlines()

lines = [l.split() for l in lines]
lines = [[float(x) for x in l] for l in lines]
src_lengths = [len(l.split()) for l in src_lines]

src_tag_probs = [[l[0]] for l, i in zip(lines, src_lengths)]
src_probs = [l[1:i+1] for l, i in zip(lines, src_lengths)]
tgt_tag_probs = [[l[i+1]] for l, i in zip(lines, src_lengths)]
tgt_probs = [l[i+2:] for l, i in zip(lines, src_lengths)]


def lines2ppl(prob_lines):
    count = sum([len(pl) for pl in prob_lines])
    log_prob = sum([sum(pl) for pl in prob_lines])
    return np.exp(-log_prob / count)


src_tag_ppl = lines2ppl(src_tag_probs)
src_ppl = lines2ppl(src_probs)
tgt_tag_ppl = lines2ppl(tgt_tag_probs)
tgt_ppl = lines2ppl(tgt_probs)

print("src-tag: {:.4f}\tsrc-ppl: {:.4f}\ttgt-tag: {:.4f}\ttgt-ppl: {:.4f}".format(
    src_tag_ppl,
    src_ppl,
    tgt_tag_ppl,
    tgt_ppl
))
