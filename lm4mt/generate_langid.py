import sys


langid = sys.argv[1]
bias = int(sys.argv[2])
for line in sys.stdin:
    print(' '.join([langid] * (len(line.strip().split()) + bias)))
