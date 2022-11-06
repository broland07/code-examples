#/bin/bash

szoveg="fajl vege"
file="szoveg.txt"

if ! [ -f "$file" ]
        then echo "$file" nem letezik vagy nem szabalyos file
        exit 1
fi

if [ -w "$file" ]
then
        echo "$szoveg" >> "$file"
else
        echo "$file" nem irhato
fi
