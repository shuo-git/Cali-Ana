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

DIR=/apdcephfs/share_916081/vinceswang/results/wmt14_en_de_stanford_ada_cali_big/score/sample_status
for step in {2000..300000..2000};do
	for SUBSET in valid test;do
		extract_fd $DIR/status_${SUBSET}_${step}.txt
	done
done