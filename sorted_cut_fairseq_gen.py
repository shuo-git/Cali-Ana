import sys

idx = int(sys.argv[1])
lines = []
for line in sys.stdin:
	line = line.strip().split('\t')
	num = int(line[0].split('-')[1])
	prob = float(line[1])
	sent = line[idx]
	lines.append((num, prob, sent))

lines = sorted(lines, key=lambda x: (x[0], -x[1]))
for line in lines:
	print(line[-1])
