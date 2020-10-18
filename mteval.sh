DISK1=/apdcephfs/private_vinceswang
DISK_DATA=$DISK1/DATASET
DISK_CODE=$DISK1/code/fairseq-T
DATA=wmt20-zhen-thu/fairseq-data
CALI=$DISK1/code/Cali-Ana
MOSES=$DISK1/tools/mosesdecoder
ORG=$DISK_DATA/wmt20-zhen-thu/devtest/sgm

SRC=zh
TGT=en

postproc() {
    # usage: postproc system lang
    if [[ "$2" = "en" ]]; then
        sed -r 's/(@@ )|(@@ ?$)//g' < $1 | \
        $MOSES/scripts/recaser/detruecase.perl |
        $MOSES/scripts/tokenizer/detokenizer.perl -l $TGT > $1.post
    elif [[ "$2" = "zh" ]]; then
        sed -r 's/(@@ )|(@@ ?$)//g' < $1 | python $CALI/misc.py > $1.post
    fi
}

filename=$1
SUBSET=${filename%%_*}

if [ "$SUBSET" = "valid" ]; then
    YEAR=19
else
    YEAR=20
fi

# sacreBLEU
postproc $filename $TGT

cat $filename.post | sacrebleu -t wmt$YEAR -l $SRC-$TGT -w 2 | tee $filename.bleu
# --tokenize zh

# multi-bleu
#BLEU=/disk1/code/fairseq-T/scripts/multi-bleu.perl
#REF=$DISK_DATA/wmt20-zhen-thu/devtest/sgm/newstest20$YEAR-enzh-src.en.txt
#
#$BLEU $REF < $filename | tee $filename.bleu