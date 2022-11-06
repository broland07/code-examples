#!/bin/bash

read -p "Kérlek add meg az átlagod(egész szám): " atlag

if [ $atlag -ge 9 ]
then
        echo "Nagyon jó"

elif [ $atlag -ge 7 ]
then
        echo "Nem rossz"

elif [ $atlag -ge 5 ]
then
        echo "Lehetne jobb is!"
else
        echo "Rossz"
fi
