import utils
import nltk
import sys
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Select the oracle translation in beam")

    parser.add_argument("--hyp", help="Path to the hypothesis file")
    parser.add_argument("--ref", help="Path to the reference file")
    parser.add_argument("--out", help="Path to the output file")
    parser.add_argument("--beam", type=int, default=1,
                        help="Beam size when generating hyp")

    return parser.parse_args()


def main(args):
    hyp_lines = utils.file2lines(args.hyp)
    if args.ref:
        ref_lines = utils.file2lines(args.ref)
    res_lines = []
    for idx in range(0, len(hyp_lines), args.beam):
        if args.ref:
            max_bleu = -1
            max_seq = None
            max_idx = -1
            for bi in range(args.beam):
                temp_bleu = nltk.translate.bleu_score.sentence_bleu([ref_lines[int(idx/args.beam)].split()],
                                                                    hyp_lines[idx+bi].split())
                if temp_bleu > max_bleu:
                    max_bleu = temp_bleu
                    max_seq = hyp_lines[idx+bi]
                    max_idx = bi
        else:
            max_idx = 0
            max_seq = hyp_lines[idx]
        print(max_idx)
        res_lines.append(max_seq)

    utils.lines2file(res_lines, args.out)


if __name__ == '__main__':
    main(parse_args())
