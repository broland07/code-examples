#!/bin/bash
# https://szerverlabor.hu/ - roland@szerverlabor.hu
file='hello.txt'
while read line; do
echo $line
done < $file
