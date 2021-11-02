#!/bin/bash
# Pega o historico COTAHIST_total completao e separa tudo bonitinho com base no ativos_anocorrente.txt ,
# criando as pastas E separando os ativos E ordenando por data.
# por <theodamontanha@gmail.com>
# em 02nov2021

ativos=../../historicoacoes/ativos_2021.txt
COTAHIST=../../historicoacoes/COTAHIST_pos_1997_ate_2021.txt
mkdir ../DADOS_B3
destino=../DADOS_B3

for ativo in $(cat $ativos); do
    cat $COTAHIST | grep $ativo >$destino/$ativo.txt

done

ls -lh $destino

exit 0
