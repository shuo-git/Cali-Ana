#!/bin/bash

CALI=/disk1/code/Cali-Ana
InfECE=/disk1/code/InfECE
TER=/disk1/tools/tercom-0.7.25
DATA=/apdcephfs/private_vinceswang/DATASET/wmt14_en_de_stanford_sampled/100w
TGTDICT=$DATA/data-bin/dict.de.txt


split(){
    python $CALI/split_corpus.py --corpus $1 --split 10000
}

bleu(){
    REF=$1
    HYP=$2
    for i in {0..9999};do
        /disk1/tools/multi-bleu.perl $REF.$i < $HYP.$i >> $HYP.bleulist
    done

    cat $HYP.bleulist | cut -d ' ' -f3 | cut -d ',' -f1 > $HYP.bleulist.figure
}

ter_ece(){
    REF=$1
    HYP=$2
    PROB=$3
    for i in {0..9999};do
        echo $i
        python $CALI/delete_eos.py $PROB.$i
        python $InfECE/add_sen_id.py $REF.$i $REF.$i.ref
        python $InfECE/add_sen_id.py $HYP.$i $HYP.$i.hyp
        java -jar $TER/tercom.7.25.jar -r $REF.$i.ref -h $HYP.$i.hyp -n $HYP.$i -s | grep TER | cut -d ' ' -f3 >> $HYP.terlist
        python $InfECE/parse_xml.py $HYP.$i.xml $HYP.$i.shifted
        python $InfECE/shift_back.py $HYP.$i.shifted.text $HYP.$i.shifted.label $HYP.$i.pra
        rm $REF.$i.ref $HYP.$i.hyp $HYP.$i.ter $HYP.$i.sum $HYP.$i.sum_nbest \
            $HYP.$i.pra_more $HYP.$i.pra $HYP.$i.xml $HYP.$i.shifted.text \
            $HYP.$i.shifted.label $HYP.$i.shifted.text.sb
        mv $HYP.$i.shifted.label.sb $HYP.$i.label
        python $InfECE/calc_ece.py \
            --prob $PROB.$i.noeos \
            --trans $HYP.$i \
            --label $HYP.$i.label \
            --vocabulary $TGTDICT \
            --bins 20 \
            --partition uniform >> $HYP.calilist
        rm $PROB.$i.noeos
    done
}


NUM=10000
REFDIR=$DATA/ref
HYPDIR=$DATA/search

#bleu $REFDIR/split$NUM/train.de $HYPDIR/split$NUM/train.4-1.de
ter_ece $REFDIR/split$NUM/train.de $HYPDIR/split$NUM/train.4-1.de $HYPDIR/split$NUM/train.4-1.de.prob