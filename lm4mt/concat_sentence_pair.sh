CODE=/home/ws/Cali-Ana/lm4mt/concat_sentence_pair.py
DATA=/data/private/ws/projects/LM4MT/data/translation/wmt14_en_de_gpt2


for pref in train valid test;do
    python $CODE --src-tag "<EN>" --tgt-tag "<DE>" \
        --src-corpus $DATA/$pref.en --tgt-corpus $DATA/$pref.de \
        --output-corpus $DATA/lm4mt/$pref.en-de
done

