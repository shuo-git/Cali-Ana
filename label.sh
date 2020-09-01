DISK1=/apdcephfs/private_vinceswang
DISK2=/apdcephfs/share_916081/vinceswang
DISK_DATA=$DISK1/DATASET
DISK_CODE=$DISK1/code/fairseq-T
SRC=en
TGT=de
SRC_VOCAB=$DISK1/DATASET/wmt14_en_de_stanford/data-bin/dict.$SRC.txt
TGT_VOCAB=$DISK1/DATASET/wmt14_en_de_stanford/data-bin/dict.$TGT.txt

CALI=$DISK1/code/Cali-Ana
InfECE=$DISK1/code/InfECE
TER=$DISK1/tools/tercom-0.7.25

ter(){
    # usage: ter ref hyp
    ref=$1
    hyp=$2
    python ${InfECE}/add_sen_id.py ${ref} ${ref}.ref
    python ${InfECE}/add_sen_id.py ${hyp} ${hyp}.hyp

    java -jar ${TER}/tercom.7.25.jar -r ${ref}.ref -h ${hyp}.hyp -n ${hyp} -s > /dev/null

    python ${InfECE}/parse_xml.py ${hyp}.xml ${hyp}.shifted
    python ${InfECE}/shift_back.py ${hyp}.shifted.text ${hyp}.shifted.label ${hyp}.pra

    rm ${ref}.ref ${hyp}.hyp ${hyp}.ter ${hyp}.sum ${hyp}.sum_nbest \
        ${hyp}.pra_more ${hyp}.pra ${hyp}.xml ${hyp}.shifted.text \
        ${hyp}.shifted.label ${hyp}.shifted.text.sb
    mv ${hyp}.shifted.label.sb ${hyp}.TER
}

ter $1 $2