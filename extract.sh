# !/bin/bash
CODE=./
extract_gen(){
	GEN=$1
	grep ^T $GEN | python3 $CODE/sorted_cut_fairseq_gen.py 1 > $GEN.ref
	grep ^H $GEN | python3 $CODE/sorted_cut_fairseq_gen.py 2 > $GEN.sys
	grep ^P $GEN | python3 $CODE/sorted_cut_fairseq_gen.py 1 > $GEN.prob
}

extract_fd(){
	FD=$1
	python3 $CODE/extract_force_dec.py $FD
}
ROOT=/apdcephfs/share_916081/vinceswang/results/wmt14_en_de_stanford_big_scale_dynamic
DIR1=$ROOT/inference
DIR2=$ROOT/score/sample_status
for step in {2000..30000..2000};do
	for SUBSET in valid test;do
		extract_gen $DIR1/${SUBSET}_${step}.gen
		extract_fd $DIR2/status_${SUBSET}_${step}.txt
	done
done