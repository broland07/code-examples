#!/bin/bash

read -p "Kérlek adj meg egy 10-nél nagyobb számot: " input

if [ $input -gt 10 ]
then
        echo "Helyes!"
else
        echo "Helytelen!"
fi