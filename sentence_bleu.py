import nltk
import utils
import sys
from nltk.translate.bleu_score import SmoothingFunction


chencherry = SmoothingFunction()

score = nltk.translate.bleu_score.sentence_bleu

refs = utils.file2words(sys.argv[1])
hyps = utils.file2words(sys.argv[2])

for r, h in zip(refs, hyps):
    print('{:.4f}'.format(score([r], h, smoothing_function=chencherry.method1)))
