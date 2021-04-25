import argparse
import numpy
import sys
from utils import *


def parse_args():
    parser = argparse.ArgumentParser(description="Concat parallel sentence pairs")

    parser.add_argument("--src-tag", required=True, type=str)
    parser.add_argument("--src-end-tag", required=False, type=str)
    parser.add_argument("--tgt-tag", required=True, type=str)
    parser.add_argument("--tgt-end-tag", required=False, type=str)
    parser.add_argument("--src-corpus", required=True, type=str)
    parser.add_argument("--output-corpus", required=True, type=str)

    return parser.parse_args()


def main(args):
    src_tag = args.src_tag
    tgt_tag = args.tgt_tag
    if args.src_end_tag is not None:
        src_end_tag = ' ' + args.src_end_tag
    else:
        src_end_tag = ''
    if args.tgt_end_tag is not None:
        tgt_end_tag = ' ' + args.tgt_end_tag
    else:
        tgt_end_tag = ''
    src_lines = file2lines(args.src_corpus)

    fw = open(args.output_corpus, 'w')

    for sl in src_lines:
        temp_sl = sl.strip()
        temp_ol = src_tag + ' ' + temp_sl + src_end_tag + ' ' + tgt_tag + '\n'
        fw.write(temp_ol)

    fw.close()


if __name__ == '__main__':
    main(parse_args())
