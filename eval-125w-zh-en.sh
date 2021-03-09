#!/bin/bash

DISK=/data/private/ws
CALI=/home/ws/Cali-Ana
MOSES=$DISK/tools/mosesdecoder
MULTI_BLEU=$MOSES/scripts/generic/multi-bleu.perl

SRC=zh
TGT=en

SUBSET=$1

postproc() {
    # usage: cat file | postproc lang
    if [[ "$1" = "en" ]]; then
        sed -r 's/(@@ )|(@@ ?$)//g'
    elif [[ "$1" = "zh" ]]; then
        sed -r 's/(@@ )|(@@ ?$)//g' | python $CALI/misc.py
    fi
}
#$MOSES/scripts/recaser/detruecase.perl | \
#$MOSES/scripts/tokenizer/detokenizer.perl -l $1

DATA=$DISK/DATASET/125w/bitext/dev_test/nist0$SUBSET/nist0$SUBSET.en

postproc $TGT | $MULTI_BLEU -lc $DATA
