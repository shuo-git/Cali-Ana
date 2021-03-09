import utils
import nltk
import sys
import argparse
import numpy as np


def parse_args():
    parser = argparse.ArgumentParser(description="Select the oracle translation in beam")

    parser.add_argument("--hyp", help="Path to the hypothesis file")
    parser.add_argument("--ref", help="Path to the reference file")
    parser.add_argument("--prob", help="Path to the probability file")
    parser.add_argument("--beam", type=int, default=1,
                        help="Beam size when generating hyp")

    return parser.parse_args()


def main(args):
    hyp_lines = utils.file2lines(args.hyp)
    if args.ref:
        ref_lines = utils.file2lines(args.ref)
    if args.prob:
        prob_lines = utils.file2words(args.prob)
    for i, l in enumerate(prob_lines):
        prob_lines[i] = np.mean([float(x) for x in l])
    for idx in range(0, len(hyp_lines), args.beam):
        

    utils.lines2file(res_lines, args.out)


if __name__ == '__main__':
    main(parse_args())
