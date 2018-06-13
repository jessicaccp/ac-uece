# instrucao rs
rs = ['jr', 'mthi', 'mtlo']

# instrucao rd
rd = ['mfhi', 'mflo']

# instrucao rt, rd
rt_fs = ['cfc1', 'ctc1', 'mfc1', 'mtc1']
rt_rd = ['cfc2', 'ctc2', 'mfc0', 'mtc0']

# instrucao rd, rs
rd_rs = ['clo', 'clz']

# instrucao rs, rt
rs_rt = ['div', 'divu', 'mult', 'multu', 'teq', 'tge', 'tgeu', 'tlt', \
'tltu', 'tne', 'madd', 'maddu', 'msub', 'msubu']

# instrucao rd, rs, rt
rd_rs_rt = ['add', 'addu', 'and', 'movn', 'movz', 'mul', 'nor', 'or', \
'slt', 'sltu', 'sub', 'subu', 'xor']

# instrucao rd, rt, rs
rd_rt_rs = ['sllv', 'srav', 'srlv']

# instrucao rd, rs, cc
rd_rs_cc = ['movf', 'movt']

# instrucao rd, rt, shamt
rd_rt_sa = ['sll', 'sra', 'srl']

# instrucao imm
offset = ['b']

# instrucao rt, imm
rt_imm = ['lui']

# instrucao rs, imm
rs_imm = ['teqi', 'tgei', 'tgeiu', 'tlti', 'tltiu', 'tnei']
rs_offset = ['bal', 'bgez', 'bgezal', 'bgezall', 'bgezl', 'bgtz', \
'bgtzl', 'blez', 'blezl', 'bltz', 'bltzal', 'bltzall', 'bltzl']

# instrucao rt, rs, imm
rt_rs_imm = ['addi', 'addiu', 'andi', 'ori', 'slti', 'sltiu', 'xori']

# instrucao rs, rt, imm
rs_rt_offset = ['beq', 'beql', 'bne', 'bnel']

# instrucao rt, imm(rs)
rt_offset_base = ['cache', 'lb', 'lbu', 'lh', 'lhu', 'll', 'lw', \
'lwl', 'lwr', 'sb', 'sc', 'sh', 'sw', 'swl', 'swr', 'ldc2', 'lwc2', \
'sdc2', 'swc2']
hint_offset_base = ['pref']
ft_offset_base = ['ldc1', 'lwc1', 'sdc1', 'swc1']

# instrucao shamt, rd
fd_fs = ['abs.s', 'abs.d', 'ceil.w.s', 'ceil.w.d', 'cvt.d.s', \
'cvt.d.w', 'cvt.d.l', 'cvt.s.d', 'cvt.s.w', 'cvt.s.l', 'cvt.w.s', \
'cvt.w.d', 'floor.w.s', 'floor.w.d', 'mov.s', 'mov.d', 'neg.s', \
'neg.d', 'round.w.s', 'round.w.d', 'sqrt.s', 'sqrt.d', 'trunc.w.s', \
'trunc.w.d']

# instrucao shamt, rd, rt
fd_fs_ft = ['add.s', 'add.d', 'div.s', 'div.d', 'mul.s', 'mul.d', \
'sub.s', 'sub.d']
fd_fs_rt = ['movn.s', 'movn.d', 'movz.s', 'movz.d']

# instrucao shamt, rd, cc
fd_fs_cc = ['movf.s', 'movf.d', 'movt.s', 'movt.d']

# instrucao
inst = ['break', 'syscall', 'deret', 'eret', 'nop', 'ssnop', 'tlbp', \
'tlbr', 'tlbwi', 'tlbwr', 'wait']

# instrucao target
target = ['j', 'jal']

# instrucao code
code = ['sdbbp']

# instrucao func
func = ['cop2']