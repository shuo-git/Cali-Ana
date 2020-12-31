import numpy as np
import argparse
import random


def parser_args():
    parser = argparse.ArgumentParser(description="Mix two corpora at sentence level")

    parser.add_argument("--pref1", help="source original")
    parser.add_argument("--pref2", help="target original")
    parser.add_argument("--pref-out", help="mixed output")
    parser.add_argument("--src", "-s")
    parser.add_argument("--tgt", "-t")
    parser.add_argument("--dropout1", type=float, default=0.)
    parser.add_argument("--dropout2", type=float, default=0.)

    return parser.parse_args()


def main(args):
    with open(args.pref1 + '.' + args.src, 'r', encoding='UTF-8') as fr:
        src_lines_1 = fr.readlines()

    with open(args.pref1 + '.' + args.tgt, 'r', encoding='UTF-8') as fr:
        tgt_lines_1 = fr.readlines()

    with open(args.pref2 + '.' + args.src, 'r', encoding='UTF-8') as fr:
        src_lines_2 = fr.readlines()

    with open(args.pref2 + '.' + args.tgt, 'r', encoding='UTF-8') as fr:
        tgt_lines_2 = fr.readlines()

    num_lines = len(src_lines_1)
    assert num_lines == len(tgt_lines_1)
    assert num_lines == len(src_lines_2)
    assert num_lines == len(tgt_lines_2)

    fw_src = open(args.pref_out + '.' + args.src, 'w', encoding='UTF-8')
    fw_tgt = open(args.pref_out + '.' + args.tgt, 'w', encoding='UTF-8')

    for i in range(num_lines):
        if random.uniform(0, 1) < args.dropout2:
            fw_src.write(src_lines_1[i])
            fw_tgt.write(tgt_lines_1[i])
        elif random.uniform(0, 1) < args.dropout1:
            fw_src.write(src_lines_2[i])
            fw_tgt.write(tgt_lines_2[i])
        else:
            fw_src.write(src_lines_1[i].rstrip() + ' ' + src_lines_2[i])
            fw_tgt.write(tgt_lines_2[i].rstrip() + ' ' + tgt_lines_1[i])

            fw_src.write(src_lines_2[i].rstrip() + ' ' + src_lines_1[i])
            fw_tgt.write(tgt_lines_2[i].rstrip() + ' ' + tgt_lines_1[i])

    fw_src.close()
    fw_tgt.close()


if __name__ == '__main__':
    main(parser_args())
