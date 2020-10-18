# !/bin/bash
DISK1=/apdcephfs/private_vinceswang
InfECE=$DISK1/code/InfECE
vocab=$DISK1/DATASET/wmt14_en_de_stanford/data-bin/dict.de.txt
CODE=$DISK1/code/Cali-Ana
DISK2=/apdcephfs/share_916081/vinceswang
# ROOT=$DISK2/results/wmt14-en-de/reduce-inference-ece/$1
ROOT=$DISK2/results/wmt14-en-de/$1
DIR1=$ROOT/inference
DIR2=$ROOT/score/sample_status

extract_gen(){
	# usage: extract_gen $1
	GEN=$1
	grep ^T $GEN | python3 $CODE/sorted_cut_fairseq_gen.py 1 > $GEN.ref
	grep ^H $GEN | python3 $CODE/sorted_cut_fairseq_gen.py 2 > $GEN.sys
	grep ^P $GEN | python3 $CODE/sorted_cut_fairseq_gen.py 1 > $GEN.prob
}

ngram_ece(){
    # usage: inf_ece $1
    GEN=$1
    ref=$GEN.ref
    hyp=$GEN.sys
    prob=$GEN.prob

    python $CODE/delete_eos.py ${prob}
    prob=$GEN.prob.noeos

    python $InfECE/n_gram_ece.py \
        --hyp $hyp \
        --ref $ref \
        --prob $prob \
        --bins 20 \
        --partition uniform

    rm $prob
}

filename=$2

#extract_gen $DIR1/${filename}
#ngram_ece $DIR1/${filename}

extract_gen ${filename}
ngram_ece ${filename}

# usage: ./main.sh base(exp_info) GEN
