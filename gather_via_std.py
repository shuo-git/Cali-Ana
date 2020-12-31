import nmtconf.utils.common as utils
import argparse
import numpy
import sys


def parse_args():
    parser = argparse.ArgumentParser(description="Gather lines according to indices")

    parser.add_argument("--label", required=True, help="Path to the indices file")

    return parser.parse_args()


def main(args):
    label = utils.file2words(args.label)
    label = [int(x[0]) for x in label]

    idx = 0
    for line in sys.stdin:
        if label[idx] == 1:
            print(line.strip())
        idx += 1


if __name__ == '__main__':
    main(parse_args())
