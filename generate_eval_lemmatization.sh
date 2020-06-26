fairseq-generate data-bin/lemmatization4 \
    --path checkpoints/checkpoint_best.pt \
    --batch-size 128 --beam 5 --remove-bpe
