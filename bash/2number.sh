#!/bin/bash
# https://szerverlabor.hu/ - roland@szerverlabor.hu
echo 'First Number :'
read a
echo 'Second Number :'
read b
x=$(expr "$a" + "$b")
echo $a + $b = $x
