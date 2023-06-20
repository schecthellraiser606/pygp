!#/bin/bash

python3 keygen.py -n $1 -e $1 -p aaa --public-key-file public.pem --private-key-file private.pem
echo "\n"
python3 sign.py -m "test taksec message" --private-key-file private.pem -p aaa
echo "\n"
cat public.pem
