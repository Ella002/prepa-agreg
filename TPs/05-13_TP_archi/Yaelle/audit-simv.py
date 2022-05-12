archi=32  # architecture 32 bits
nb_reg=32 # nombre de registre du banc de registres

# La mémoire est modélisée comme une liste de mot de 8b
mem = []

def init_mem(prog=None):
    for inst in prog:
        i = GenInst.parse_instruction(inst)
        mem.append(i[0:8])
        mem.append(i[8:16])
        mem.append(i[16:24])
        mem.append(i[24:32])

def fetch(addr):

    return mem[addr.to_uint()] + \
        mem[addr.to_uint()+1] + \
        mem[addr.to_uint()+2] + \
        mem[addr.to_uint()+3]

def mux_RX(opcode):
    # selection de l'opérande X de l'alu
    if opcode  in [b'1100100', b'1100011', b'1110011']:
        return banc[decodeur.rs1.to_uint()]
    elif opcode in [b'1100110', b'1110100']:
        return PC.lecture()
    else:
        print("mux_RX: opcode ({opcode}) non supporté")
        raise NotImplemented

def mux_RY(opcode, funct3):
    # selection de l'opérande Y de l'alu
    if opcode  in [b'1100110', b'1100011']:
        return banc[decodeur.rs2.to_uint()]
    if opcode  in [b'1100100']:
        if funct3.to_bytes() in [b'100', b'101']:
            return BitArray(decodeur.imm[0:5].to_uint(), archi)
        else:
            return BitArray(decodeur.imm.to_bytes(), archi)
    elif opcode in [b'1110100']:
        return BitArray(b'0', 12) + decodeur.imm
    elif opcode in [b'1110011']:
        return BitArray(decodeur.imm.to_bytes(), archi)
    else:
        print("mux_RY: opcode ({opcode}) non supporté")
        raise NotImplemented

def writeback(opcode, funct3):
    # mise à jour banc de registres
    if opcode in [b'1100110', b'1100100']:
        if funct3.to_bytes() == b'010':
            return BitArray(alu.sign and alu.overflow, archi)
        if funct3.to_bytes() == b'110':
            return  BitArray(alu.sign and not alu.carry, archi)
        else:
            return alu.res
    elif opcode in [b'1111011', b'1110011']:
        return BitArray(PC.lecture().to_int()+4, archi)
    elif opcode in [b'1100011']:
        pass
    elif opcode in [b'1110100']:
        return alu.res
    elif opcode in [b'1110110']:
        return BitArray(b'0', 12) + decodeur.imm

def cycle():
    """
    Effectue les opération d'un cycle CPU
    """

    ############## Fetch      ################################
    IR.ecriture(fetch(PC.lecture()))

    ############## Decode     ################################
    # decode l'instruction présente dans IR et configure l'ALU
    decodeur.decode(IR.lecture())
    opcode = decodeur.opcode.to_bytes()

    ############## Exec       ################################
    # Execute l'instruction
    # si opération arithmétiques:
    if decodeur.alu_op is not None:
        # selection de l'opérande X de l'alu
        x = mux_RX(opcode)

        # selection de l'opérande Y de l'alu
        y = mux_RY(opcode, decodeur.funct3)

        alu.eval(decodeur.alu_op, x, y)

    ############## Write Back ################################
    if opcode not in [b'1100011']:
        banc[decodeur.rd.to_uint()] = writeback(opcode, decodeur.funct3)

    # Mise à jour de PC
    PC.ecriture(update_PC(decodeur, PC.lecture(), alu))

if __name__ == '__main__':
    init_mem(fibo)

    # les registres CPU
    IR = Registre(archi)
    PC = Registre(archi)
    banc = BancRegistre(nb_reg, archi)

    # les differentes unité du CPU
    decodeur = Decodeur()
    alu = Alu()

    # Initialisation de PC
    PC.ecriture(BitArray(b'00000000000000000000000000000000'))

    try:
        while True:
            cycle()
    except IndexError:
        print("Fin du programme")
        print(banc)
        print(f"IR: {IR.lecture()}\t {decode_instruction(IR.lecture())}")
        print(f"PC: {PC.lecture()}")
