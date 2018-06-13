# primeiro a ser checado.
# checa os bits 31:26 / linha[0:6]
op = {2: 'j', 3: 'jal', 4: 'beq', 5: 'bne', 6: 'blez', 7: 'bgtz', \
8: 'addi', 9: 'addiu', 10: 'slti', 11: 'sltiu', 12: 'andi', 13: 'ori', \
14: 'xori', 15: 'lui', 20: 'beql', 21: 'bnel', 22: 'blezl', \
23: 'bgtzl', 32: 'lb', 33: 'lh', 34: 'lwl', 35: 'lw', 36: 'lbu', \
37: 'lhu', 38: 'lwr', 40: 'sb', 41: 'sh', 42: 'swl', 43: 'sw', \
46: 'swr', 47: 'cache', 48: 'll', 49: 'lwc1', 50: 'lwc2', 51: 'pref', \
53: 'ldc1', 54: 'ldc2', 56: 'sc', 57: 'swc1', 58: 'swc2', 61: 'sdc1', \
62: 'sdc2'}

# se op = 16, 17 ou 18 (z = 0, 1 ou 2, respectivamente),
# checa os bits 25:21 / linha[6:11]
rs_z = {0: 'mfc', 2: 'cfc', 4: 'mtc', 6: 'ctc', 16: 'cop', 17: 'cop'}

# se op = 1,
# checa os bits 20:16 / linha[11:16]
rt_op1 = {0: 'bltz', 1: 'bgez', 2: 'bltzl', 3: 'bgezl', 8: 'tgei', \
9: 'tgeiu', 10: 'tlti', 11: 'tltiu', 12: 'tegi', 14: 'tnei', \
16: 'bltzal', 17: 'bgezal', 18: 'bltzall', 19: 'bgczall'}

# se z = 1 ou 2,
# checa os bits 17:16 / linha[14:16]
# obs: seja x = linha[14:16] em decimal,
# a instrucao tem o formato 'bc' + z + bc[x] / exemplo: bc1f
bc = {0: 'f', 1: 't', 2: 'fl', 3: 'tl'}

# se op = 0 e funct_op0 = 1,
# checa os bits 16:16 / linha[15:16]
mov_f1 = {0: 'movf', 1: 'movt'}

# se funct = 17,
# checa os bits 16:16 / linha[15:16]
# obs: seja x = linha[15:16] em decimal,
# a instrucao tem o formato mov_f17[x] + f / exemplo: movf.d
mov_f17 = {0: 'movf.', 1: 'movt.'}

# se op = 0,
# checa os bits 5:0 / linha[26:32]
funct_op0 = {0: 'sll', 2: 'srl', 3: 'sra', 4: 'sllv', 6: 'srlv', \
7: 'srav', 8: 'jr', 9: 'jalr', 10: 'movz', 11: 'movn', 12: 'syscall', \
13: 'break', 15: 'sync', 16: 'mfhi', 17: 'mthi', 18: 'mflo', \
19: 'mtlo', 24: 'mult', 25: 'multu', 26: 'div', 27: 'divu', 32: 'add', \
33: 'addu', 34: 'sub', 35: 'subu', 36: 'and', 37: 'or', 38: 'xor', \
39: 'nor', 42: 'slt', 43: 'sltu', 48: 'tge', 49: 'tgeu', 50: 'tlt', \
51: 'tltu', 52: 'teq', 54: 'tne'}

# se rs = 17 (se z = 1, f = d; se z = 2, f = s),
# checa os bits 5:0 / linha[26:32]
# obs: seja x = linha[26:32] em decimal,
# a instrucao tem o formato funct_rs17[x] + f / exemplo: add.d
funct_rs17 = {0: 'add.', 1: 'sub.', 2: 'mul.', 3: 'div.', 4: 'sqrt.', \
5: 'abs.', 6: 'mov.', 7: 'neg.', 12: 'round.w.', 13: 'trunc.w.', \
14: 'cell.w.', 15: 'floor.w.', 18: 'movz.', 19: 'movn.', 32: 'cvt.s.', \
33: 'cvt.d.', 36: 'cvt.w.', 48: 'c.f.', 49: 'c.un.', 50: 'c.eq.', \
51: 'c.ueq.', 52: 'c.olt.', 53: 'c.ult.', 54: 'c.ole.', 55: 'c.ule.', \
56: 'c.sf.', 57: 'c.ngle.', 58: 'c.seq.', 59: 'c.ngl.', 60: 'c.lt.', \
61: 'c.nge.', 62: 'c.le.', 63: 'c.ngt.'}

# se op = 28,
# checa os bits 5:0 / linha[26:32]
funct_op28 = {0: 'madd', 1: 'maddu', 2: 'mul', 4: 'msub', 5: 'msubu', \
32: 'clz', 33: 'clo'}

# se z = 0,
# checa os bits 4:0 / linha[27:32]
funct_z0 = {1: 'tlbr', 2: 'tlbwi', 6: 'tlbwr', 8: 'tlbp', 24: 'eret', \
31: 'deret'}