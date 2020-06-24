#!/usr/bin/env bash
#
# Adapted from https://github.com/facebookresearch/MIXER/blob/master/prepareData.sh

echo 'Cloning Moses github repository (for tokenization scripts)...'
git clone https://github.com/moses-smt/mosesdecoder.git

echo 'Cloning Subword NMT repository (for BPE pre-processing)...'
git clone https://github.com/rsennrich/subword-nmt.git

SCRIPTS=mosesdecoder/scripts
TOKENIZER=$SCRIPTS/tokenizer/tokenizer.perl
LC=$SCRIPTS/tokenizer/lowercase.perl
CLEAN=$SCRIPTS/training/clean-corpus-n.perl
BPEROOT=subword-nmt/subword_nmt
BPE_TOKENS=10000

src=before
tgt=after
lang=before-after
prep=tokenized.before-after
tmp=$prep/tmp
orig=orig

mkdir -p $orig $tmp $prep

for l in $src $tgt; do
    f=train.$l
    tok=train.$lang.tok.$l

    cat ./$f | \
    perl $TOKENIZER -threads 8 -l pl > $tmp/$tok
    echo ""
done

perl $CLEAN -ratio 1.5 $tmp/train.$lang.tok $src $tgt $tmp/train.$lang 1 175

for l in $src $tgt; do
    f=test.$l
    tok=test.$lang.tok.$l

    cat ./$f | \
    perl $TOKENIZER -threads 8 -l pl > $tmp/$tok
    echo ""
done

for l in $src $tgt; do
    f=valid.$l
    tok=valid.$lang.tok.$l

    cat ./$f | \
    perl $TOKENIZER -threads 8 -l pl > $tmp/$tok
    echo ""
done

BPE_CODE=$prep/code

echo "learn_bpe.py ..."
python $BPEROOT/learn_bpe.py -s $BPE_TOKENS < $tmp/train.before-after > $BPE_CODE

for L in $src $tgt; do
    for f in train.before-after.tok.$L valid.before-after.tok.$L test.before-after.tok.$L; do
        echo "apply_bpe.py to ${f}..."
        python $BPEROOT/apply_bpe.py -c $BPE_CODE < $tmp/$f > $tmp/bpe.$f
    done
done

perl $CLEAN -ratio 1.5 $tmp/bpe.train.before-after.tok $src $tgt $prep/train 1 250
perl $CLEAN -ratio 1.5 $tmp/bpe.valid.before-after.tok $src $tgt $prep/valid 1 250

for L in $src $tgt; do
    cp $tmp/bpe.test.before-after.tok.$L $prep/test.$L
done
