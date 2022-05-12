from bitArray import BitArray
from format_inst import Format

inst_list = ['addi 1,0,1',
             'addi 2,0,1',
             'addi 3,0,1',
             'addi 4,0,1',
             'addi 5,0,1',
             'addi 6,0,1']

table_opcode = {
    # Arithmetique et logique
    'add':  {'opcode': b'1100110', 'funct3': 0x0, 'funct7': 0x00},
    'sub':  {'opcode': b'1100110', 'funct3': 0x0, 'funct7': 0x20},
    'xor':  {'opcode': b'1100110', 'funct3': 0x4, 'funct7': 0x00},
    'or':   {'opcode': b'1100110', 'funct3': 0x6, 'funct7': 0x00},
    'and':  {'opcode': b'1100110', 'funct3': 0x7, 'funct7': 0x00},
    'slt':  {'opcode': b'1100110', 'funct3': 0x2, 'funct7': 0x00},
    'sltu': {'opcode': b'1100110', 'funct3': 0x3, 'funct7': 0x00},
    'sll':  {'opcode': b'1100110', 'funct3': 0x1, 'funct7': 0x00},
    'srl':  {'opcode': b'1100110', 'funct3': 0x5, 'funct7': 0x00},
    'sra':  {'opcode': b'1100110', 'funct3': 0x5, 'funct7': 0x20},
    # immediat
    'addi':  {'opcode': b'1100100', 'funct3': 0x0},
    'xori':  {'opcode': b'1100100', 'funct3': 0x4},
    'ori':   {'opcode': b'1100100', 'funct3': 0x6},
    'andi':  {'opcode': b'1100100', 'funct3': 0x7},
    'slti':  {'opcode': b'1100100', 'funct3': 0x2},
    'sltiu': {'opcode': b'1100100', 'funct3': 0x3},
    'slli':  {'opcode': b'1100100', 'funct3': 0x1, 'funct7': 0x00},
    'srli':  {'opcode': b'1100100', 'funct3': 0x5, 'funct7': 0x00},
    'srai':  {'opcode': b'1100100', 'funct3': 0x5, 'funct7': 0x20},
    # Branchement Conditionnel
    'beq':   {'opcode': b'1100011', 'funct3': 0x0},
    'bne':   {'opcode': b'1100011', 'funct3': 0x1},
    'blt':   {'opcode': b'1100011', 'funct3': 0x4},
    'bge':   {'opcode': b'1100011', 'funct3': 0x5},
    'bltu':  {'opcode': b'1100011', 'funct3': 0x6},
    'bgeu':  {'opcode': b'1100011', 'funct3': 0x7},
    # Branchement et lien
    'jal':   {'opcode': b'1111011'},
    'jalr':  {'opcode': b'1110011', 'funct3': 0x0},
    # Chargement d'immédiat
    'lui':   {'opcode': b'1110110'},
    'auipc': {'opcode': b'1110100'}
}

class GenInst:

    def parse_instruction(inst):
        name, args = inst.split(' ')

        # OP sur registre: Arithmeatique et logique, comparaison, décalage
        # "nom RD,RS1,RS2" ⇒ format R
        if name in ['add', 'sub', 'xor', 'or', 'and',
                    'slt', 'sltu', 'sll', 'srl', 'sra']:
            rd, rs1, rs2 = args.split(',')
            inst = BitArray(table_opcode[name]['opcode']) + BitArray(int(rd), 5) + \
                BitArray(table_opcode[name]['funct3'], 3) + \
                BitArray(int(rs1), 5) + BitArray(int(rs2), 5) + \
                BitArray(table_opcode[name]['funct7'], 7)

            # OP sur immedia: Arithmeatique et logique, comparaison, décalage et jalr
            # "nom RD,RS1,imm" ⇒ format I
        elif name in ['addi', 'xori', 'ori', 'andi', 'slti', 'sltiu',
                      'jalr']:
            rd, rs1, imm = args.split(',')

            inst = BitArray(table_opcode[name]['opcode']) + BitArray(int(rd), 5) + \
                BitArray(table_opcode[name]['funct3'], 3) + \
                BitArray(int(rs1), 5) + BitArray(int(imm), 12)

        elif name in ['slli', 'srli']:
            rd, rs1, imm = args.split(',')

            inst = BitArray(table_opcode[name]['opcode']) + BitArray(int(rd), 5) + \
                BitArray(table_opcode[name]['funct3'], 3) + \
                BitArray(int(rs1), 5) + BitArray(int(imm), 5) + BitArray(0, 7)

        elif name in ['srai']:
            rd, rs1, imm = args.split(',')

            inst = BitArray(table_opcode[name]['opcode']) + BitArray(int(rd), 5) + \
                BitArray(table_opcode[name]['funct3'], 3) + \
                BitArray(int(rs1), 5) + BitArray(int(imm), 5) + BitArray(0x20, 7)

            # Branchement Conditionnel:
            # "nom RS1,RS2,imm" ⇒ format B
        elif name in ['beq', 'bne', 'blt', 'bge', 'bltu', 'bgeu']:
            rs1, rs2, imm = args.split(',')
            bimm = BitArray(int(imm), 13)
            inst = BitArray(table_opcode[name]['opcode']) + bimm[11:12] + bimm[1:5] + \
                BitArray(table_opcode[name]['funct3'], 3) + \
                BitArray(int(rs1), 5) + BitArray(int(rs2), 5) + bimm[5:11] + bimm[12:13]

            # jal
            # "jal RD,imm" ⇒ Format J
        elif name in ['jal']:
            rd, imm = args.split(',')
            bimm = BitArray(int(imm), 21)
            inst = BitArray(table_opcode[name]['opcode']) + BitArray(int(rd), 5) + \
                bimm[12:20] + \
                bimm[11:12] + \
                bimm[1:11] + \
                bimm[20:21]

            # lui/auipc
            # "lui/auipc RD,imm" ⇒ Format U
        elif name in ['lui', 'auipc']:
            rd, imm = args.split(',')
            inst = BitArray(table_opcode[name]['opcode']) + BitArray(int(rd), 5) + \
                BitArray(int(imm), 20)
        else:
            raise NotImplemented(f"Operation {name} non implementée.")

        return inst

def decode_instruction(inst):
    for key in table_opcode:
        if table_opcode[key]['opcode'] == Format.opcode(inst).to_bytes():
            if table_opcode[key]['opcode'] in [b'1111011', b'1110110', b'1110100']:
                # nmémonique ne dépend que de l'opcode
                return f"{key} {Format.rd(inst).to_uint()},{Format.imm(inst).to_bytes()}"
            elif table_opcode[key]['funct3'] == Format.funct3(inst).to_uint():
                # nmémonique dépendent de l'opcode et de funct3
                if table_opcode[key]['opcode'] in [b'1110100']:
                    return f"{key} {Format.rd(inst).to_uint()},{Format.rs1(inst).to_uint()},{Format.imm(inst).to_bytes()}"
                elif table_opcode[key]['opcode'] in [b'1110011']:
                    # jalr
                    return f"{key} {Format.rd(inst).to_uint()},{Format.rs1(inst).to_uint()},{Format.imm(inst).to_bytes()}"
                elif table_opcode[key]['opcode'] in [b'1100011']:
                    # branchement conditionnel
                    return f"{key} {Format.rs1(inst).to_uint()},{Format.rs2(inst).to_uint()},{Format.imm(inst).to_bytes()}"
                elif table_opcode[key]['opcode'] in [b'1100100']:
                    if table_opcode[key]['funct3'] in [0x0, 0x4, 0x6, 0x7, 0x2, 0x3]:
                        return key + " " + str(Format.rd(inst).to_uint()) +\
                            "," + str(Format.rs1(inst).to_uint()) + "," + str(Format.imm(inst).to_bytes())
                    elif table_opcode[key]['funct7'] == Format.funct7(inst).to_uint():
                        return key + " " + str(Format.rd(inst).to_uint()) +\
                            "," + str(Format.rs1(inst).to_uint()) + "," + str(Format.imm(inst).to_bytes())
                elif table_opcode[key]['opcode'] in [b'1100110']:
                    if table_opcode[key]['funct3'] == Format.funct3(inst).to_uint() and table_opcode[key]['funct7'] == Format.funct7(inst).to_uint():
                        return key + " " + str(Format.rd(inst).to_uint()) +\
                            "," + str(Format.rs1(inst).to_uint()) + "," + str(Format.rs2(inst).to_uint())

    return f"Instruction non reconnue opcode:{Format.opcode(inst).to_bytes()}, funct3:{Format.funct3(inst).to_bytes()}, funct7:{Format.funct7(inst).to_bytes()}"
