#!/bin/bash
# https://szerverlabor.hu/ - roland@szerverlabor.hu
echo -n "Enter a filename to see last modification time : "
read fileName
 
if [ ! -f $fileName ]
then
 echo "$fileName not a file"
 exit 1
fi
 
echo "$fileName was last modified on $(stat -c %x $fileName)"