import sys
from utils import *


filename=sys.argv[1]
lines = file2words(filename)
res_lines = [l[:-1] for l in lines]
words2file(res_lines, filename + '.noeos')
