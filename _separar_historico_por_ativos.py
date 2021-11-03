#!/usr/bin/python3
# A partir do historico COTAHIST_1994 e do arquivo de
# 'ativos' do ano corrente, controi historico de cada ativo.
# Em 02nov2021.

# Não ta servindo para nada, nao funciona.

arqHistorico = '/mnt/arquivos/python_projetos/historicoacoes/COTAHIST_so_2021.txt'
historico = open(arqHistorico, 'r', encoding="ISO-8859-1")

arqListaAtivos = '/mnt/arquivos/python_projetos/historicoacoes/ativos_2021.txt'
listaAtivos = open(arqListaAtivos, 'r', encoding="ISO-8859-1")
ativos = []


for ativo in listaAtivos:
    ativos.append(ativo.strip())
    # print(ativo.strip())

cumprimentoAtivos = len(ativos)

for linha in historico:
    for ativo in ativos:
        if str(ativo) in linha:
            print(linha.strip())

        # print(ativos)
        # print('Quebra')
        # print(ativos)


print('O tamanho da lista é: ' + str(cumprimentoAtivos))
historico.close()
listaAtivos.close()
exit()
