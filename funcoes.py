from formatos import *
from instrucoes import *

# lista com os nomes dos 32 registradores
# reg[0] == '$zero', reg[1] == '$at' e assim sucessivamente
reg = ['$zero', '$at', '$v0', '$v1', '$a0', '$a1', '$a2', '$a3', \
'$t0', '$t1', '$t2', '$t3', '$t4', '$t5', '$t6', '$t7', '$s0', '$s1', \
'$s2', '$s3', '$s4', '$s5', '$s6', '$s7', '$t8', '$t9', '$k0', '$k1', \
'$gp', '$sp', '$fp', '$ra']

# recebe uma linha do arquivo de entrada e a lista text,
# decifra qual a instrucao da linha e adiciona seu nome na lista text
def decifrar_instrucao(linha, text):

    # valores transformados de binario para decimal
    # necessarios para identificar a instrucao
    op_linha = int(linha[0:6], 2)
    rs_linha = int(linha[6:11], 2)
    rt_linha = int(linha[11:16], 2)
    funct_linha = int(linha[26:32], 2)
    bc_linha = int(linha[14:16], 2)
    mov_linha = int(linha[15:16], 2)
    funct5_linha = int(linha[27:32], 2)
    func_linha = int(linha[7:32], 2)

    # com base no mips opcode map e nos dicionarios, decifra a instrucao
    if op_linha == 0:
        if funct_linha == 1:
            instrucao = mov_f1[mov_linha]
        else:
            instrucao = funct_op0[funct_linha]
    elif op_linha == 1:
        instrucao = rt_op1[rt_linha]
    elif op_linha == 16:
        z = 0
        if rs_linha == 16:
            instrucao = funct_z0[funct5_linha]
        else:
            instrucao = rs_z[rs_linha]
            instrucao += z
    elif op_linha == 17:
        z = 1
        if rs_linha == 8:
            instrucao = bc[bc_linha]
            instrucao = 'bc' + z + instrucao
        elif rs_linha == 16:
            f = 's'
            if funct_linha == 17:
                instrucao = mov_f17[mov_linha]
            else:
                instrucao = funct_rs17[func_linha]
            instrucao += f
        elif rs_linha == 17:
            f = 'd'
            if funct_linha == 17:
                instrucao = mov_f17[mov_linha]
            else:
                instrucao = funct_rs17[func_linha]
            instrucao += f
        else:
            instrucao = rs_z[rs_linha]
            instrucao += z
    elif op_linha == 18:
        z = 2
        if rs_linha == 8:
            instrucao = bc[bc_linha]
            instrucao = 'bc' + z + instrucao
        else:
            instrucao = rs_z[rs_linha]
            instrucao += z
    elif op_linha == 28:
        instrucao = funct_op28[funct_linha]
    else:
        instrucao = op[op_linha]

    # adiciona o nome da instrucao na lista text
    text.append(instrucao)

# recebe uma linha do .data do arquivo de entrada,
# transforma pra decimal e adiciona o valor na lista data
def coletar_data(linha, data):
    data.append(int(linha, 2))

# de acordo com o indice da lista text recebido,
# le o nome da instrucao, detecta o formato e os valores
# que acompanharao a instrucao e atualiza a linha na lista text. /
# nas instrucoes de jump e branch, detecta os saltos e os salva em uma
# lista chamada saltos, no formato (id, indice de text destino do salto)
def formatar_instrucao(linha, indice, text, data, saltos, n_saltos):
    
    # valores transformados de binario para decimal
    # necessarios para formatar a instrucao
    rs_linha = int(linha[6:11], 2)
    rt_linha = int(linha[11:16], 2)
    rd_linha = int(linha[16:21], 2)
    shamt_linha = int(linha[21:26], 2)
    imm_linha = int(linha[16:32], 2)
    imm_neg_linha = imm_linha - (1<<16)
    cc_linha = int(linha[11:14], 2)
    target_linha = int(linha[6:32], 2)
    code_linha = int(linha[6:26], 2)
    func_linha = int(linha[7:32], 2)

    instrucao = text[indice]    # nome da instrucao
    pc = indice*4               # contador de programa

    # formatos:
    # instrucao reg[rs]
    if instrucao in rs:
        text[indice] += (9 - len(instrucao))*' ' + reg[rs_linha]

    # instrucao reg[rd]
    elif instrucao in rd:
        text[indice] += (9 - len(instrucao))*' ' + reg[rd_linha]

    # instrucao reg[rt], reg[rd] / instrucao reg[rt], reg[fs]
    elif instrucao in (rt_rd + rt_fs):
        text[indice] += (9 - len(instrucao))*' ' + reg[rt_linha] + \
        (5 - len(reg[rt_linha]))*' ' + '\t' + reg[rd_linha]

    # instrucao reg[rd], reg[rs]
    elif instrucao in rd_rs:
        text[indice] += (9 - len(instrucao))*' ' + reg[rd_linha] + \
        (5 - len(reg[rd_linha]))*' ' + '\t' + reg[rs_linha]

    # instrucao reg[rs], reg[rt]
    elif instrucao in rs_rt:
        text[indice] += (9 - len(instrucao))*' ' + reg[rs_linha] + \
        (5 - len(reg[rs_linha]))*' ' + '\t' + reg[rt_linha]

    # instrucao reg[rd], reg[rs], reg[rt]
    elif instrucao in rd_rs_rt:
        text[indice] += (9 - len(instrucao))*' ' + reg[rd_linha] + \
        (5 - len(reg[rd_linha]))*' ' + '\t' + reg[rs_linha] + \
        (5 - len(reg[rs_linha]))*' ' + '\t' + reg[rt_linha]

    # instrucao reg[rd], reg[rt], reg[rs]
    elif instrucao in rd_rt_rs:
        text[indice] += (9 - len(instrucao))*' ' + reg[rd_linha] + \
        (5 - len(reg[rd_linha]))*' ' + '\t' + reg[rt_linha] + \
        (5 - len(reg[rt_linha]))*' ' + '\t' + reg[rs_linha]

    # instrucao reg[rd], reg[rs], reg[cc]
    elif instrucao in rd_rs_cc:
        text[indice] += (9 - len(instrucao))*' ' + reg[rd_linha] + \
        (5 - len(reg[rd_linha]))*' ' + '\t' + reg[rs_linha] + \
        (5 - len(reg[rs_linha]))*' ' + '\t' + reg[cc_linha]

    # instrucao reg[rd], reg[rt], sa
    elif instrucao in rd_rt_sa:
        text[indice] += (9 - len(instrucao))*' ' + reg[rd_linha] + \
        (5 - len(reg[rd_linha]))*' ' + '\t' + reg[rt_linha] + \
        (5 - len(reg[rt_linha]))*' ' + '\t' + str(shamt_linha)

    # instrucao offset
    elif instrucao in offset:
        n_saltos += 1   # atualiza o numero de saltos

        if n_saltos < 10:
            l = 'L0'
        else:
            l = 'L'

        # salto para um pc anterior ao atual
        if imm_linha > (len(text)-indice) + 1:
            text[indice] += (9 - len(instrucao))*' ' + l + str(n_saltos)
            saltos.append((n_saltos, int((imm_neg_linha*4 + 4 + pc)/4)))
        # salto para um pc posterior ao atual
        else:
            text[indice] += (9 - len(instrucao))*' ' + l + str(n_saltos)
            saltos.append((n_saltos, int((imm_linha*4 + 4 + pc)/4)))

    # instrucao reg[rt], immediate
    elif instrucao in rt_imm:
        text[indice] += (9 - len(instrucao))*' ' + reg[rt_linha] + \
        (5 - len(reg[rt_linha]))*' ' + '\t' + str(imm_linha)

    # instrucao reg[rs], immediate
    elif instrucao in rs_imm:
        text[indice] += (9 - len(instrucao))*' ' + reg[rs_linha] + \
        (5 - len(reg[rs_linha]))*' ' + '\t' + str(imm_linha)

    # instrucao reg[rs], offset
    elif instrucao in rs_offset:
        n_saltos += 1   # atualiza o numero de saltos

        if n_saltos < 10:
            l = 'L0'
        else:
            l = 'L'

        # salto para um pc anterior ao atual
        if imm_linha > (len(text)-indice) + 1:
            text[indice] += (9 - len(instrucao))*' ' + reg[rs_linha] + \
            (5 - len(reg[rs_linha]))*' ' + '\t' + l + str(n_saltos)
            saltos.append((n_saltos, int((imm_neg_linha*4 + 4 + pc)/4)))
        # salto para um pc posterior ao atual
        else:
            text[indice] += (9 - len(instrucao))*' ' + reg[rs_linha] + \
            (5 - len(reg[rs_linha]))*' ' + '\t' + l + str(n_saltos)
            saltos.append((n_saltos, int((imm_linha*4 + 4 + pc)/4)))

    # instrucao reg[rt], reg[rs], immediate
    elif instrucao in rt_rs_imm:
        text[indice] += (9 - len(instrucao))*' ' + reg[rt_linha] + \
        (5 - len(reg[rt_linha]))*' ' + '\t' + reg[rs_linha] + \
        (5 - len(reg[rs_linha]))*' ' + '\t' + str(imm_linha)

    # instrucao reg[rs], reg[rt], offset
    elif instrucao in rs_rt_offset:
        n_saltos += 1   # atualiza o numero de saltos

        if n_saltos < 10:
            l = 'L0'
        else:
            l = 'L'

        # salto para um pc anterior ao atual
        if imm_linha > (len(text)-indice) + 1:
            text[indice] += (9 - len(instrucao))*' ' + reg[rs_linha] + \
            (5 - len(reg[rs_linha]))*' ' + '\t' + reg[rt_linha] + \
            (5 - len(reg[rt_linha]))*' ' + '\t' + l + str(n_saltos)
            saltos.append((n_saltos, int((imm_neg_linha*4 + 4 + pc)/4)))
        # salto para um pc posterior ao atual
        else:
            text[indice] += (9 - len(instrucao))*' ' + reg[rs_linha] + \
            (5 - len(reg[rs_linha]))*' ' + '\t' + reg[rt_linha] + \
            (5 - len(reg[rt_linha]))*' ' + '\t' + l + str(n_saltos)
            saltos.append((n_saltos, int((imm_linha*4 + 4 + pc)/4)))

    # instrucao reg[rt], offset(reg[base]) /
    # instrucao reg[hint], offset(reg[base]) /
    # instrucao reg[ft], offset(reg[base])
    elif instrucao in (rt_offset_base + hint_offset_base + \
    ft_offset_base):
        # se rs == 0, procura um valor em .data
        if reg[rs_linha] == '$zero':
            # atualiza imm_linha para o indice
            # correspondente da lista data + 1
            imm_linha = int((imm_linha - 8192) / 4) + 1
            if imm_linha > len(data):
                text[indice] += (9 - len(instrucao))*' ' + \
                reg[rt_linha] + (5 - len(reg[rt_linha]))*' ' + '\t' + \
                str(imm_linha) + '(' + reg[rs_linha] + ')'
            elif imm_linha < 10:
                text[indice] += (9 - len(instrucao))*' ' + \
                reg[rt_linha] + (5 - len(reg[rt_linha]))*' ' + '\t' + \
                'V0' + str(imm_linha)
            else:
                text[indice] += (9 - len(instrucao))*' ' + \
                reg[rt_linha] + (5 - len(reg[rt_linha]))*' ' + '\t' + \
                'V' + str(imm_linha)
        # senao, nao atualiza o valor de imm_linha
        else:
            text[indice] += (9 - len(instrucao))*' ' + reg[rt_linha] + \
            (5 - len(reg[rt_linha]))*' ' + '\t' + str(imm_linha) + \
            '(' + reg[rs_linha] + ')'

    # instrucao reg[fd], reg[fs]
    elif instrucao in fd_fs:
        text[indice] += (9 - len(instrucao))*' ' + reg[shamt_linha] + \
        (5 - len(reg[shamt_linha]))*' ' + '\t' + reg[rd_linha]

    # instrucao reg[fd], reg[fs], reg[ft] /
    # instrucao reg[fd], reg[fs], reg[rt]
    elif instrucao in (fd_fs_ft + fd_fs_rt):
        text[indice] += (9 - len(instrucao))*' ' + reg[shamt_linha] + \
        (5 - len(reg[shamt_linha]))*' ' + '\t' + reg[rd_linha] + \
        (5 - len(reg[rd_linha]))*' ' + '\t' + reg[rt_linha]

    # instrucao reg[fd], reg[fs], reg[cc]
    elif instrucao in fd_fs_cc:
        text[indice] += (9 - len(instrucao))*' ' + reg[shamt_linha] + \
        (5 - len(reg[shamt_linha]))*' ' + '\t' + reg[rd_linha] + \
        (5 - len(reg[rd_linha]))*' ' + '\t' + reg[cc_linha]

    # instrucao / nao precisa de alteracao
    elif instrucao in inst:
        pass

    # instrucao target
    elif instrucao in target:
        n_saltos += 1   # atualiza o numero de saltos

        if n_saltos < 10:
            l = 'L0'
        else:
            l = 'L'

        text[indice] += (9 - len(instrucao))*' ' + l + str(n_saltos)
        saltos.append((n_saltos, int(target_linha)))

    # instrucao code
    elif instrucao in code:
        text[indice] += (9 - len(instrucao))*' ' + str(code_linha)

    # instrucao func
    elif instrucao in func:
        text[indice] += (9 - len(instrucao))*' ' + str(func_linha)

    # mensagem de erro
    else:
        print('Erro ao formatar instrucao')

    # retorna o numero de saltos atualizado, caso tenha ocorrido algum
    return n_saltos

# para cada linha em text, checa em saltos se existe um salto para
# aquela linha. / se sim, adiciona a marcacao no comeco da linha. /
# se nao, apenas alinha com o restante do text. / obs: no caso da
# primeira linha nao ser destino de salto, marca como 'main'
def formatar_saltos(text, saltos):
    for t in range(0, len(text)):
        flag = True
        for s in saltos:
            if t == s[1]:
                if s[0] < 10:
                    text[t] = 'L0' + str(s[0]) + ':  \t' + text[t]
                else:
                    text[t] = 'L' + str(s[0]) + ':  \t\t' + text[t]
                flag = False
                break
        if flag:
            if t == 0:
                text[t] = 'main:\t' + text[t]
            else:
                text[t] = '     \t' + text[t]

    for s in saltos:
        if s[1] == len(text):
            if s[0] < 10:
                text.append('L0' + str(s[0]) + ':')
            else:
                text.append('L' + str(s[0]) + ':')

# atualiza todas as linhas de data para que
# fiquem no formato final requerido
def formatar_data(data):
    v = 1
    for i in range(0, len(data)):
        if v<10:
            data[i] = 'V0' + str(v) + ':\t.word\t' + str(data[i])
        else:
            data[i] = 'V' + str(v) + ':\t.word\t' + str(data[i])
        v += 1

# abre o arquivo de saida e salva as linhas de text e data nele
def imprimir(text, data):
    saida = open('output', 'w')

    # .text
    saida.write('.text\n')
    print('.text')
    for linha in text:
        saida.write(str(linha) + '\n')
        print(linha)
    
    # se existir, .data
    if len(data) > 0:
        saida.write('\n.data\n')
        print('\n.data')
        for linha in data:
            saida.write(str(linha) + '\n')
            print(linha)

    saida.close()
