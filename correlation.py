import numpy as np
import pandas as pd
import argparse
from utils import *


def parser_args():
    parser = argparse.ArgumentParser(description="Calculate the Pearson correlation of input arrays")

    parser.add_argument("--cali", help="Path to the calibration file")
    parser.add_argument("--idx-cali", type=int, default=0,
                        help="Index of the interested column in the calibration file")
    parser.add_argument("--gene", help="Path to the generation quality file")
    parser.add_argument("--idx-gene", type=int, default=0,
                        help="Index of the interested column in the generation quality file")
    parser.add_argument("--num-lines", type=int, default=0,
                        help="Number of lines used to calculate the correlation")


    return parser.parse_args()


def main(args):
    cali = file2words(args.cali)
    gene = file2words(args.gene)
    if args.num_lines > 0:
        cali = cali[:args.num_lines]
        gene = gene[:args.num_lines]
    cali = list(zip(*cali))[args.idx_cali]
    gene = list(zip(*gene))[args.idx_gene]
    cali = [float(x) for x in cali]
    gene = [float(x) for x in gene]

    data = pd.DataFrame({'Cali': cali, 'Gene': gene})

    print(data.corr()['Cali']['Gene'])


if __name__ == '__main__':
    main(parser_args())
