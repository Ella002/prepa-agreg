# erreur
from geninst import GenInst
from geninst import decode_instruction
from registre import Registre
from banc_reg import BancRegistre
from decodeur import Decodeur
from alu import Alu
from bitArray import BitArray
from update_PC import update_PC

archi=32  # architecture 32 bits
nb_reg=32 # nombre de registre du banc de registres

# La mémoire est modélisée comme une liste de mot de 8b
mem = []

def init_mem(prog = None):
    """
    init_mem(prog) initialise la memoire en y stockant
    l'encodage machine de chaque instruction de prog
    """

    # erreur
    if prog is None:
        raise NotImplemented

    for inst in prog:
        i = GenInst.parse_instruction(inst)
        mem.append(i[0:8])
        mem.append(i[8:16])
        mem.append(i[16:24])
        mem.append(i[24:32])

def fetch(addr):
    """
    fetch(addr) recupere le mot stocke en memoire a addr
    """
    return mem[addr.to_uint()] + \
        mem[addr.to_uint()+1] + \
        mem[addr.to_uint()+2] + \
        mem[addr.to_uint()+3]

def mux_RX(opcode):
    """
    mux_RX(opcode) renvoie la valeur de l'operande X,
    etant donnes l'opcode et le decodeur
    """
    # selection de l'opérande X de l'alu
    # erreur. 1100110 est l'opcode des operations de format R, qui lisent rs1
    # if opcode  in [b'1100100', b'1100011', b'1110011']:
    if opcode in [b'1100110', b'1100100', b'1100011', b'1110011']:
        # format R, I, B et jalr
        return banc[decodeur.rs1.to_uint()]
    # elif opcode in [b'1100110', b'1110100']:
    elif opcode in [b'1110100']:
        # auipc
        return PC.lecture()
    else:
        print("mux_RX: opcode ({opcode}) non supporté")
        raise NotImplemented

def mux_RY(opcode, funct3):
    """
    mux_RY(opcode) renvoie la valeur de l'operande Y,
    etant donnes l'opcode et le decodeur
    """
    # selection de l'opérande Y de l'alu
    if opcode  in [b'1100110', b'1100011']:
        # format R et B
        return banc[decodeur.rs2.to_uint()]
    if opcode  in [b'1100100']:
        # format I
        if funct3.to_bytes() in [b'100', b'101']:
            # slli et srai: imm est sur bits 0..4
            return BitArray(decodeur.imm[0:5].to_uint(), archi)
        else:
            # Rq: on peut juste renvoyer decodeur.imm
            return BitArray(decodeur.imm.to_bytes(), archi)
    elif opcode in [b'1110100']:
        # auipc: y = imm << 12
        return BitArray(b'0', 12) + decodeur.imm
    elif opcode in [b'1110011']:
        # jalr
        return BitArray(decodeur.imm.to_bytes(), archi)
    else:
        print("mux_RY: opcode ({opcode}) non supporté")
        raise NotImplemented

def writeback(opcode, funct3):
    """
    writeback(opcode, funct3) renvoie la valeur a stocker dans rd,
    s'il y en a une, en fonction de l'opcode, funct3, alu, decodeur
    """
    # mise à jour banc de registres
    if opcode in [b'1100110', b'1100100']:
        # format R et I
        if funct3.to_bytes() == b'010':
            # slt et slti: on ecrit 1 si <, 0 sinon
            return BitArray(alu.sign and alu.overflow, archi)
        if funct3.to_bytes() == b'110':
            # sltu et sltiu
            return  BitArray(alu.sign and not alu.carry, archi)
        else:
            return alu.res
    elif opcode in [b'1111011', b'1110011']:
        # jal et jalr: rd <- PC + 4
        return BitArray(PC.lecture().to_int()+4, archi)
    elif opcode in [b'1100011']:
        # format B: pas de writeback?
        pass
    elif opcode in [b'1110100']:
        # auipc
        return alu.res
    elif opcode in [b'1110110']:
        # lui: rd <- imm << 12
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

fibo = ['addi 1,0,10', # n <- 10
        'addi 2,0,2',  # i <- 1
        'addi 3,0,1',  # ui_2 <- 1
        'addi 4,0,1',  # ui_1 <- 1
        'beq 0,0,20',  # goto cond
        'add 5,3,4',   # ui <- ui_2 + ui_1
        'add 3,4,0',   # ui_2 <- ui_1
        'add 4,5,0',   # ui_1 <- ui
        'addi 2,2,1',  # i <- i+1
        'blt 2,1,-16']

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
