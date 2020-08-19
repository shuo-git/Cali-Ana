# !/bin/bash
DISK1=/apdcephfs/private_vinceswang
InfECE=$DISK1/code/InfECE
TER=$DISK1/tools/tercom-0.7.25
vocab=$DISK1/DATASET/wmt14_en_de_stanford/data-bin/dict.de.txt
CODE=./
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

extract_fd(){
	# usage: extract_fd $1
	FD=$1
	python3 $CODE/extract_force_dec.py $FD
}

inf_ece(){
    # usage: inf_ece $1
    GEN=$1
    ref=$GEN.ref
    hyp=$GEN.sys
    prob=$GEN.prob

    python $CODE/delete_eos.py ${prob}
    prob=$GEN.prob.noeos

    # echo "Generating TER label..."
    python ${InfECE}/add_sen_id.py ${ref} ${ref}.ref
    python ${InfECE}/add_sen_id.py ${hyp} ${hyp}.hyp

    java -jar ${TER}/tercom.7.25.jar -r ${ref}.ref -h ${hyp}.hyp -n ${hyp} -s > /dev/null

    python ${InfECE}/parse_xml.py ${hyp}.xml ${hyp}.shifted
    python ${InfECE}/shift_back.py ${hyp}.shifted.text ${hyp}.shifted.label ${hyp}.pra

    rm ${ref}.ref ${hyp}.hyp ${hyp}.ter ${hyp}.sum ${hyp}.sum_nbest \
        ${hyp}.pra_more ${hyp}.pra ${hyp}.xml ${hyp}.shifted.text \
        ${hyp}.shifted.label
    mv ${hyp}.shifted.text.sb ${hyp}.sb
    mv ${hyp}.shifted.label.sb ${hyp}.label

    # echo "Filtering unaligned tokens..."
    for f in ${hyp} ${hyp}.label ${prob};do
        if [ ${f} = ${hyp} ]
        then
            python ${InfECE}/filter_diff_tok.py ${hyp} ${hyp}.sb ${f} > /dev/null
        else
            python ${InfECE}/filter_diff_tok.py ${hyp} ${hyp}.sb ${f} > /dev/null
        fi
    done

    # echo "Calculating inference ECE..."
    # prepare4relia.py
    # calc_ece.py
    python ${InfECE}/calc_ece.py \
        --prob ${prob}.filt \
        --trans ${hyp}.filt \
        --label ${hyp}.label.filt \
        --vocabulary ${vocab} \
        --bins 20 \
        --partition uniform

    rm ${hyp}.filt ${hyp}.label.filt ${prob}.filt
}

train_ece(){
    # train_ece $1 $2
    FD=$1
    SUBSET=$2

    python $CODE/delete_eos.py $FD.prob
    python $CODE/delete_eos.py $FD.acc

    python ${InfECE}/calc_ece.py \
        --prob $FD.prob.noeos \
        --trans $DIR2/$SUBSET.de \
        --label $FD.acc.noeos \
        --vocabulary ${vocab} \
        --bins 20 \
        --partition uniform
}

filename=$2
if [ "$3" = "train" ]
then
    extract_fd $DIR2/${filename}
    train_ece $DIR2/${filename} $4
else
    extract_gen $DIR1/${filename}
    inf_ece $DIR1/${filename}
fi
# usage: ./main.sh base(exp_info) GEN train/inf
