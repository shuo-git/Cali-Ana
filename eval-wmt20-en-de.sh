#!/bin/bash

DISK1=/apdcephfs/private_vinceswang
DISK2=/apdcephfs/share_916081/vinceswang
DISK_DATA=$DISK2/DATASET
DISK_CODE=$DISK1/code/fairseq
DATA=$DISK_DATA/wmt20-en-de
CALI=$DISK1/code/Cali-Ana
MOSES=$DISK1/tools/mosesdecoder

SRC=en
TGT=de

filename=$1

if [ $2 = 14 ]; then
    YEAR="14/full"
else
    YEAR=$2
fi

#tok_ref=$DATA/newstest/$SRC-$TGT/$2/test.tok.$TGT
#
#cat $filename | sed -r 's/(@@ )|(@@ ?$)//g' | \
#    $MOSES/scripts/generic/multi-bleu.perl $tok_ref

cat $filename | sed -r 's/(@@ )|(@@ ?$)//g' | \
    $MOSES/scripts/tokenizer/detokenizer.perl -l $TGT | \
    sacrebleu -t wmt$YEAR -l $SRC-$TGT -w 1 --detail