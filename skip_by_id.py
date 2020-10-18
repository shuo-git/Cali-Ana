import sys

idx = 0
skipped = [134124, 228280]
for line in sys.stdin:
    if not idx in skipped:
        print(line, end='')
    idx += 1