#!/bin/bash
# Please run with arg1st is string. exp: ./sandworm "test"

python3 keygen.py -n "taksec" -e "$1" -p aaa --public-key-file public.pem --private-key-file private.pem
python3 sign.py -m "test taksec message" --private-key-file private.pem -p aaa
cat public.pem
