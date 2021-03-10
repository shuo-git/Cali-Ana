CODE=/home/ws/Cali-Ana/lm4mt/concat_sentence_pair_inf.py
DATA=/data/private/ws/projects/LM4MT/data/translation/wmt14_en_de


for pref in valid test;do
    python $CODE --src-tag "<EN>" --tgt-tag "<DE>" \
        --src-corpus $DATA/$pref.en \
        --output-corpus $DATA/lm4mt/inference/$pref.en-de
done

