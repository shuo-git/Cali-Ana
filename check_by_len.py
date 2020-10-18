import sys

if len(sys.argv) > 3:
	sft = int(sys.argv[3])
else:
	sft = 0

whether_pass = True
with open(sys.argv[1], 'r', encoding='utf-8') as fr1, \
     open(sys.argv[2], 'r', encoding='utf-8') as fr2:
    lines1 = fr1.readlines()
    lines2 = fr2.readlines()
    if lines1[-1].strip() == '':
        del lines1[-1]
    if lines2[-1].strip() == '':
        del lines2[-1]
    assert len(lines1) == len(lines2)
    i = 0
    for line1, line2 in zip(lines1, lines2):
        i += 1
        if not len(line1.split())+sft == len(line2.split()):
            print("{} {} {}".format(i, len(line1.split()), len(line2.split())))
            whether_pass = False
    if whether_pass:
        print("Pass")
