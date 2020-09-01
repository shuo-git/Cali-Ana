import sys
import numpy as np
from utils import *


def gather_ngrams(scores):
    """
    :param scores: list of list (num_examples, num_grams)
    :return:
    """
    res_list = []
    for sl in scores:
        res_list.append(np.exp(np.sum(np.log(sl) * np.array([0.1, 0.2, 0.3, 0.4]))))
        # res_list.append(np.mean(sl))
    return res_list


if __name__ == '__main__':
    scores = file2words(sys.argv[1])
    scores = [[float(x) for x in l[0:4]] for l in scores]
    res_scores = gather_ngrams(scores)
    res_scores = ['{:.4f}\n'.format(x) for x in res_scores]
    lines2file(res_scores, sys.argv[2])
