import sys
import argparse
import os
from utils import *


def parser_args():
    parser = argparse.ArgumentParser(description="Split the whole corpus into several subsets")

    parser.add_argument("--corpus", help="Path to the whole corpus")
    parser.add_argument("--split", type=int, default=100,
                        help="Number of splits")

    return parser.parse_args()


def main(args):
    all_lines = file2lines(args.corpus)
    num_lines = len(all_lines)
    capacity = int(num_lines / args.split)

    dest_dir = '{}/{}{}'.format(os.path.dirname(args.corpus), 'split', args.split)

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    prefix = '{}/{}'.format(dest_dir, os.path.basename(args.corpus))

    for i in range(0, num_lines, capacity):
        idx = int(i / capacity)
        fw = open('{}.{}'.format(prefix, idx), 'w')
        fw.writelines(all_lines[i:i+capacity])
        fw.close()


if __name__ == '__main__':
    main(parser_args())
