from bitArray import BitArray

def update_PC(decodeur, pc, alu, archi=32):
    """update_PC renvoie la future valeur de PC en fonction de
    l'instruction courante, de la valeur courante de PC et des sorties
    de l'ALU
    """
    opcode = decodeur.opcode.to_bytes()

    if opcode == b'1100011':
        # c'est un saut conditionnel

        funct3 = decodeur.funct3.to_bytes()
        jump = False
        if funct3 == b'000':
            # beq -> jump si ZF
            jump = alu.zero

        elif funct3 == b'100':
            # bne -> jump if !ZF
            jump = not alu.zero

        elif funct3 == b'001':
            # blt -> jump if OF != SF
            jump = alu.overflow != alu.sign

        elif funct3 == b'101':
            # bge -> jump if OF = SF
            jump = alu.overflow == alu.sign

        elif funct3 == b'011':
            # bltu -> jump if CF
            jump = alu.carry

        elif funct3 == b'111':
            # bgeu -> jump if !CF
            jump = not alu.carry

        if jump:
            # PC = PC + imm
            return BitArray(pc.to_int() + decodeur.imm.to_int(), archi)
        else:
            # PC = PC + 4
            return BitArray(pc.to_int() + 4, archi)

    elif opcode == b'1111011':
        # jal -> PC = PC + imm
        return BitArray(pc.to_int() + decodeur.imm.to_int(), archi)

    elif opcode == b'1110011':
        # jalr -> PC = rs1 + imm
        # on suppose que rs1 + imm a ete calcule par l'ALU
        return alu.res

    else:
        return BitArray(pc.to_int() + 4, archi)
