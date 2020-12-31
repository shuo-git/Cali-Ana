import argparse
import numpy
import sys


def parse_args():
    parser = argparse.ArgumentParser(description="Adding Tag to files")

    parser.add_argument("--tag", required=True, type=str, help="the added tag")

    return parser.parse_args()


def main(args):
    for line in sys.stdin:
        print(args.tag + ' ' + line.strip())


if __name__ == '__main__':
    main(parse_args())
