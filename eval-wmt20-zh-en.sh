#!/bin/bash

DISK1=/apdcephfs/private_vinceswang
DISK2=/apdcephfs/share_916081/vinceswang
DISK_DATA=$DISK2/DATASET
DISK_CODE=$DISK1/code/fairseq
CALI=$DISK1/code/Cali-Ana
MOSES=$DISK1/tools/mosesdecoder

SRC=zh
TGT=en

filename=$1

SUBSET=${filename%%_*}
if [ "$SUBSET" = "valid" ]; then
    YEAR=19
else
    YEAR=20
fi

#YEAR=$2

postproc() {
    # usage: cat file | postproc lang
    if [[ "$1" = "en" ]]; then
        sed -r 's/(@@ )|(@@ ?$)//g' | \
        $MOSES/scripts/recaser/detruecase.perl | \
        $MOSES/scripts/tokenizer/detokenizer.perl -l $1
    elif [[ "$1" = "zh" ]]; then
        sed -r 's/(@@ )|(@@ ?$)//g' | python $CALI/misc.py
    fi
}


#if [[ "$TGT" = "zh" ]];then
#    cat $filename | postproc $TGT | \
#        sacrebleu -t wmt$YEAR -l $SRC-$TGT -w 1 --tokenize zh
#else
#    cat $filename | postproc $TGT | \
#        sacrebleu -t wmt$YEAR -l $SRC-$TGT -w 1
#fi


DATA=$DISK_DATA/wmt20-$TGT-$SRC/sacrebleu
cat $filename | postproc $TGT | \
    sacrebleu $DATA/$YEAR.$TGT -w 1
