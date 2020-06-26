TEXT=data-bin/lemmatization_5
fairseq-preprocess --source-lang before --target-lang after \
    --trainpref $TEXT/train --validpref $TEXT/valid --testpref $TEXT/test \
    --destdir data-bin/lemmatization5 \
    --workers 20

