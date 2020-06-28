# !/bin/bash
DISK1=/apdcephfs/private_vinceswang
InfECE=$DISK1/code/InfECE
TER=$DISK1/tools/tercom-0.7.25
vocab=$DISK1/DATASET/wmt14_en_de_stanford/data-bin/dict.de.txt

infece(){
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
    --vocabulary ${vocab} > $GEN.infece

rm ${hyp}.filt ${hyp}.label.filt ${prob}.filt
}

DISK2=/apdcephfs/share_916081/vinceswang
DIR=$DISK2/results/wmt14_en_de_stanford_ada_cali_base-bak/inference
DIR="/apdcephfs/share_916081/vinceswang/results/wmt14_en_de_stanford_ada_cali_base-bak/inference"
for step in 2000;do
	for SUBSET in valid test;do
		infece $DIR/${SUBSET}_${step}.gen
	done
done






