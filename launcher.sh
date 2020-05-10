#!/bin/bash

nsimulacoes=$1
nciclos=$2
pathSaidas="../Influenza/Espaciais"

rm -rf ${pathSaidas} 
mkdir ${pathSaidas}

for  i in $(seq 0 $(($nsimulacoes-1)));
do
    mkdir $pathSaidas"/"${i}
done

python gerador.py ${nciclos} ${nsimulacoes}