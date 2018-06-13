from formatos import *
from funcoes import *
from instrucoes import *

def main():
    text = []       # .text
    data = []       # .data
    saltos = []     # (id do salto, linha para onde deve ir)

    # abre o arquivo de entrada contendo
    # o programa em linguagem de maquina
    entrada = open('input8', 'r')

    # primeira leitura do arquivo: assumindo que .text
    # vem antes do .data e que uma linha vazia os separa. /
    # flag == True indica estar no .text,
    # flag == False indica estar no .data.
    flag = True
    for linha in entrada:
        if linha == '\n':
            flag = False
        # adiciona o nome da instrucao correspondente na lista text
        elif flag:
            decifrar_instrucao(linha, text)
        # adiciona o valor em decimal correspondente na lista data
        else:
            coletar_data(linha, data)

    # recomeca a leitura do arquivo
    entrada.seek(0,0)

    # variaveis auxiliares para a proxima leitura
    indice = 0      # indice atual da lista text
    n_saltos = 0    # numero de saltos realizados no programa

    # segunda leitura do arquivo.
    # de acordo com a instrucao presente na lista text,
    # assimila a instrucao ao seu devido formato e atualiza a lista.
    # se houver salto, atualiza a lista saltos e n_saltos.
    for linha in entrada:
        # se for verdade, acabou de ler o .text do arquivo e sai do loop
        if linha == '\n':
            break

        n_saltos = formatar_instrucao(linha, indice, text, data, \
        saltos, n_saltos)
        indice += 1 # atualiza o indice

    # checa os valores da lista saltos e adapta a lista text
    formatar_saltos(text, saltos)

    # altera a lista data para o formato do mips assembly
    formatar_data(data)

    # salva o programa traduzido para mips assembly no arquivo de saida
    imprimir(text, data)

    # fecha o arquivo de entrada e finaliza o disassembler
    entrada.close()

if __name__ == '__main__':
    main()