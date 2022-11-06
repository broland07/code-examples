#!/bin/bash
# https://szerverlabor.hu/ - roland@szerverlabor.hu

function line(){
	echo "*************************************************"
}

echo "Your username : $(echo $USER)"
line

echo "Current date and time : $(date)"
line

echo "Currently logged on users:"
who
line