#!/bin/bash
# https://szerverlabor.hu/ - roland@szerverlabor.hu
FILE="$1"

if [ $# -eq 0 ]
then
	echo "$0 file-name"
	exit 1
fi

which stat > /dev/null
 
if [ $? -eq 1 ]
then
	echo "stat command not found!"
	exit 2
fi

if [ ! -e $FILE ]
then
	echo "$FILE not a file"
	exit 3
fi

echo "Time of last access : $(stat -c %x $FILE)"
echo "Time of last modification : $(stat -c %y $FILE)"
echo "Time of last change : $(stat -c %z $FILE)"