import sys
sys.path.append('/disk1/code/Cali-Ana')
import utils
import numpy as np
import itertools


probs = utils.file2words(sys.argv[1])
probs = [[np.exp(float(w)) for w in l] for l in probs]
eos_probs = [l[-1] for l in probs]
ending_punc_probs = [l[-1] for l in probs]
other_probs = [l[:-1] for l in probs]
other_probs = list(itertools.chain(*other_probs))
avg_op = np.mean(other_probs)
avg_eosp = np.mean(eos_probs)
print('{:.4f}\t{:.4f}\t{:.4f}'.format(avg_op, avg_eosp, avg_eosp - avg_op))
