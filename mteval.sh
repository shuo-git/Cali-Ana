DISK1=/apdcephfs/private_vinceswang
DISK_DATA=$DISK1/DATASET
DISK_CODE=$DISK1/code/fairseq-T
DATA=wmt20-zhen-thu/fairseq-data
CALI=$DISK1/code/Cali-Ana
MOSES=$DISK1/tools/mosesdecoder
ORG=$DISK_DATA/wmt20-zhen-thu/devtest/sgm


postproc() {
    # usage: cat file | postproc lang
    if [[ "$1" = "zh" ]]; then
        sed -r 's/(@@ )|(@@ ?$)//g' | python $CALI/misc.py
    else
        sed -r 's/(@@ )|(@@ ?$)//g' | \
        $MOSES/scripts/recaser/detruecase.perl | \
        $MOSES/scripts/tokenizer/detokenizer.perl -l $1
    fi
}


postproc $1
