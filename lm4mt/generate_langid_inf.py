import sys


langid = sys.argv[1]
endingid = sys.argv[2]
bias = int(sys.argv[3])
for line in sys.stdin:
    print(' '.join([langid] * (len(line.strip().split()) - 1) + [endingid] * (bias + 1)))
