# !/bin/bash
DISK1=/apdcephfs/private_vinceswang
InfECE=$DISK1/code/InfECE
TER=$DISK1/tools/tercom-0.7.25
vocab=$DISK1/DATASET/wmt14_en_de_stanford/data-bin/dict.de.txt
DISK2=/apdcephfs/share_916081/vinceswang
DIR1=$DISK2/results/wmt14_en_de_stanford_big_scale_dynamic/inference
DIR2=$DISK2/results/wmt14_en_de_stanford_big_scale_dynamic/score/sample_status

inf_ece(){
GEN=$1
ref=$GEN.ref
hyp=$GEN.sys
prob=$GEN.prob

python ./delete_eos.py ${prob}
prob=$GEN.prob.noeos

echo "Generating TER label..."
python ${InfECE}/add_sen_id.py ${ref} ${ref}.ref
python ${InfECE}/add_sen_id.py ${hyp} ${hyp}.hyp

java -jar ${TER}/tercom.7.25.jar -r ${ref}.ref -h ${hyp}.hyp -n ${hyp} -s

python ${InfECE}/parse_xml.py ${hyp}.xml ${hyp}.shifted
python ${InfECE}/shift_back.py ${hyp}.shifted.text ${hyp}.shifted.label ${hyp}.pra

rm ${ref}.ref ${hyp}.hyp ${hyp}.ter ${hyp}.sum ${hyp}.sum_nbest \
    ${hyp}.pra_more ${hyp}.pra ${hyp}.xml ${hyp}.shifted.text \
    ${hyp}.shifted.label
mv ${hyp}.shifted.text.sb ${hyp}.sb
mv ${hyp}.shifted.label.sb ${hyp}.label

echo "Filtering unaligned tokens..."
for f in ${hyp} ${hyp}.label ${prob};do
    if [ ${f} = ${hyp} ]
    then
        python ${InfECE}/filter_diff_tok.py ${hyp} ${hyp}.sb ${f}
    else
        python ${InfECE}/filter_diff_tok.py ${hyp} ${hyp}.sb ${f} > /dev/null
    fi
done

echo "Calculating inference ECE..."
python ${InfECE}/calc_ece.py \
    --prob ${prob}.filt \
    --trans ${hyp}.filt \
    --label ${hyp}.label.filt \
    --vocabulary ${vocab} >> $DIR1/token-infece.log

rm ${hyp}.filt ${hyp}.label.filt ${prob}.filt
}

train_ece(){
FD=$1
SUBSET=$2

python ./delete_eos.py $FD.prob
python ./delete_eos.py $FD.acc

python ${InfECE}/calc_ece.py \
    --prob $FD.prob.noeos \
    --trans $DIR2/$SUBSET.de \
    --label $FD.acc.noeos \
    --vocabulary ${vocab} >> $DIR2/trainece.log
}

for SUBSET in valid test;do
	for step in {2000..300000..2000};do
		inf_ece $DIR1/${SUBSET}_${step}.gen
        train_ece $DIR2/status_${SUBSET}_${step}.txt $SUBSET
	done
done






