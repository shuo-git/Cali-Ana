#!/bin/bash

DISK1=/apdcephfs/private_vinceswang
DISK_DATA=$DISK1/DATASET
DISK_CODE=$DISK1/code/fairseq
DATA=$DISK_DATA/wmt14-en-de
CALI=$DISK1/code/Cali-Ana
MOSES=$DISK1/tools/mosesdecoder

SRC=en
TGT=de

filename=$1
SUBSET=${filename%%_*}
if [ "$SUBSET" = "valid" ]; then
    YEAR=13
else
    YEAR="14/full"
fi

sed -r 's/(@@ )|(@@ ?$)//g' < $filename | \
    $MOSES/scripts/recaser/detruecase.perl > $filename.tok

cat $filename.tok | \
$MOSES/scripts/generic/multi-bleu.perl $DATA/tmp/$SUBSET.tok.$TGT | tee $filename.bleu

$MOSES/scripts/tokenizer/detokenizer.perl -l $TGT < $filename.tok | \
sacrebleu -t wmt$YEAR -l $SRC-$TGT -w 2 | tee $filename.sacrebleu

rm $filename.tok
rm $filename.*bleu