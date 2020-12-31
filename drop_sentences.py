import numpy as np
import argparse
import random


def parser_args():
    parser = argparse.ArgumentParser(description="Mix two corpora at sentence level")

    parser.add_argument("--pref-in", help="source original")
    parser.add_argument("--pref-out", help="mixed output")
    parser.add_argument("--src", "-s")
    parser.add_argument("--tgt", "-t")
    parser.add_argument("-p", type=float, default=1.)

    return parser.parse_args()


def main(args):
    with open(args.pref_in + '.' + args.src, 'r', encoding='UTF-8') as fr:
        src_lines = fr.readlines()

    with open(args.pref_in + '.' + args.tgt, 'r', encoding='UTF-8') as fr:
        tgt_lines = fr.readlines()

    num_lines = len(src_lines)
    assert num_lines == len(tgt_lines)

    fw_src = open(args.pref_out + '.' + args.src, 'w', encoding='UTF-8')
    fw_tgt = open(args.pref_out + '.' + args.tgt, 'w', encoding='UTF-8')

    num_reserved = int(num_lines * args.p)

    fw_src.writelines(src_lines[:num_reserved])
    fw_tgt.writelines(tgt_lines[:num_reserved])

    fw_src.close()
    fw_tgt.close()


if __name__ == '__main__':
    main(parser_args())
