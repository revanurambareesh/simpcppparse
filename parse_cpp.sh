#!/bin/sh
lex cpplex.l
cc lex.yy.c
./a.out
echo '\n\nOutput character string\n'
cat output.txt

echo '\n'
python parse.py
