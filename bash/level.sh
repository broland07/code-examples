
#!/bin/bash
#Csekkolja a megadott parametert, majd addig megy amig meg nem talalja ujra a cat utan megadott karakterlancot.
cimzett=${1:? hianyzik az elso paramter, a cimzett neve}

cat << VEGE

Figyelmeztetés

Kedves ${cimzett}

kérjük egyenlitse ki a számláját.
Üdvözlettel,
ISP

VEGE
