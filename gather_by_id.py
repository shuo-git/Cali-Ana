import nmtconf.utils.common as utils
import argparse
import numpy


def parse_args():
    parser = argparse.ArgumentParser(description="Gather lines according to indices")

    parser.add_argument("--input", required=True, nargs="+", help="Path to the input file")
    parser.add_argument("--idx", required=True, help="Path to the indices file")
    parser.add_argument("--suffix", required=True, help="Suffix of output files")

    return parser.parse_args()


def main(args):
    stream = [open(item, 'rb') for item in args.input]
    data = [fd.readlines() for fd in stream]

    idx = utils.file2words(args.idx)
    idx = [int(x[0]) for x in idx]

    # idx = numpy.arange(len(data[0]))
    # numpy.random.shuffle(idx)

    newstream = [open(item + '.' + args.suffix, 'wb') for item in args.input]
    for i in idx:
        lines = [item[i] for item in data]
        for line, fd in zip(lines, newstream):
            fd.write(line)

    for fdr, fdw in zip(stream, newstream):
        fdr.close()
        fdw.close()


if __name__ == '__main__':
    main(parse_args())
