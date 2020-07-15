import utils as utils
import sys


def main():
    lines = utils.file2lines(sys.argv[1])
    rpt_times = int(sys.argv[2])
    res_lines = []
    for line in lines:
        for _ in range(rpt_times):
            res_lines.append(line)

    utils.lines2file(res_lines, sys.argv[1] + '.rpt' + str(rpt_times))


if __name__ == "__main__":
    main()
