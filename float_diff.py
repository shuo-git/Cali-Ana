import sys
import numpy as np
import utils


lines1 = utils.file2words(sys.argv[1])
lines2 = utils.file2words(sys.argv[2])
res_lines = []
res_sum = 0.
res_max = 0.
res_count = 0

assert len(lines1) == len(lines2)

for l1, l2 in zip(lines1, lines2):
    assert len(l1) == len(l2)
    res_lines.append([])
    for w1, w2 in zip(l1, l2):
        temp_diff = np.exp(float(w1)) - np.exp(float(w2))
        res_lines[-1].append('{:.4f}'.format(temp_diff))
        res_sum += abs(temp_diff)
        res_max = max(res_max, temp_diff)
        res_count += 1

utils.words2file(res_lines, sys.argv[3])
print('average = {:.4f}'.format(res_sum / res_count))
print('max = {:.4f}'.format(res_max))
