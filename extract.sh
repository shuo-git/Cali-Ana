# !/bin/bash
CODE=./
extract(){
	GEN=$1
	grep ^T $GEN | python3 $CODE/sorted_cut_fairseq_gen.py 1 > $GEN.ref
	grep ^H $GEN | python3 $CODE/sorted_cut_fairseq_gen.py 2 > $GEN.sys
	grep ^P $GEN | python3 $CODE/sorted_cut_fairseq_gen.py 1 > $GEN.prob
}

DIR="/apdcephfs/share_916081/vinceswang/results/wmt14_en_de_stanford_base/inference"
for step in {2000..100000..2000};do
	for SUBSET in valid test;do
		extract $DIR/${SUBSET}_${step}.gen
	done
done