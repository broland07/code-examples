#!/bin/bash

#ellenőrzés
str=${1:? nincs paraméter}

echo a paraméter hossza ${#str}
echo első karaktere: ${str:0:1}
