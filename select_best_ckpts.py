import sys


steps = []
scores = []

for line in sys.stdin:
    terms = line.split()
    for i, t in enumerate(terms):
        if t == 'bleu':
            scores.append(float(terms[i + 1]))
        elif t == 'num_updates':
            steps.append(int(terms[i + 1]))
            break

infos = list(zip(steps, scores))
infos.sort(key=lambda x: x[1], reverse=False)
for info in infos:
    # if info[0] % 500 == 0:
    print('{}\t{}'.format(info[0], info[1]))
