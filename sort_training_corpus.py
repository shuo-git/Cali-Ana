import nmtconf.utils.common as utils
import numpy as np
import sys

en_scores = utils.file2lines(sys.argv[1])
en_scores = [float(x) for x in en_scores]
zh_scores = utils.file2lines(sys.argv[2])
zh_scores = [float(x) for x in zh_scores]

scores = [x - y for x, y in zip(en_scores, zh_scores)]
scores = [(idx, x) for idx, x in enumerate(scores)]

sorted_scores = sorted(scores, key=lambda x: x[1])
sorted_indices = ['{}\t{:.2f}\n'.format(x[0], x[1]) for x in sorted_scores]
utils.lines2file(sorted_indices, sys.argv[3])