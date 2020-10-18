TEXT=$1
cat $TEXT | sed -r 's/(@@ )|(@@ ?$)//g' | /disk1/tools/mosesdecoder/scripts/tokenizer/detokenizer.perl -l de > $TEXT.plain

CUDA_VISIBLE_DEVICES=0 python /disk1/code/Cali-Ana/lm_scorer.py $TEXT.plain