import argparse
import numpy
import sys
from utils import *


def parse_args():
    parser = argparse.ArgumentParser(description="Concat parallel sentence pairs")

    parser.add_argument("--src-tag", required=True, type=str)
    parser.add_argument("--tgt-tag", required=True, type=str)
    parser.add_argument("--tgt-end-tag", required=False, type=str)

    return parser.parse_args()


def main(args):
    src_tag = args.src_tag
    tgt_tag = args.tgt_tag
    if args.tgt_end_tag is not None:
        tgt_end_tag = args.tgt_end_tag
    else:
        tgt_end_tag = None
    for line in sys.stdin:
        words = line.split()
        assert words[0] == src_tag
        for idx, w in enumerate(words):
            if w == tgt_tag:
                break
        if tgt_end_tag is not None:
            if words[-1] == tgt_end_tag:
                words = words[:-1]
        print(' '.join(words[idx+1:]))


if __name__ == '__main__':
    main(parse_args())
