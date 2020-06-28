import sys
from utils import *


def delete_pad(_list):
    res_list = []
    for item in _list:
        if item == '2.0':
            break
        res_list.append(item)
    return res_list


lines = file2lines(sys.argv[1])
lines = [l.split('|||') for l in lines]
indices = [int(l[0]) for l in lines]
probs = [delete_pad(l[1].split()) for l in lines]
accs = [delete_pad(l[2].split()) for l in lines]
data = zip(indices, probs, accs)
data.sort(key=lambda x: x[0])
indices, probs, accs = zip(*data)

words2file(probs, sys.argv[1] + '.prob')
words2file(acc, sys.argv[1] + '.acc')