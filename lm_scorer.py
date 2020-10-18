import torch
import sys
import numpy as np
import utils

# List available models
# torch.hub.list('pytorch/fairseq')  # [..., 'transformer_lm.wmt19.en', ...]

# Load an German LM trained on WMT'19 News Crawl data
de_lm = torch.hub.load('pytorch/fairseq', 'transformer_lm.wmt19.de', tokenizer='moses', bpe='fastbpe')
de_lm.eval()  # disable dropout

# Move model to GPU
de_lm.cuda()


def ppl(filename):
    lines = utils.file2lines(filename)
    corpus_probs = []
    for line in lines:
        scores = de_lm.score(line)['positional_scores']
        corpus_probs.extend(scores.tolist())
    corpus_ppl = np.exp(-np.mean(corpus_probs))
    return corpus_ppl


# print(corpus_ppl)
# utils.lines2file(prob_lines, sys.argv[2])