from decodeur import Decodeur
from registre import Registre
from banc_reg import BancRegistre
from bitArray import BitArray
from format_inst import Format
from alu import Alu
from geninst import GenInst
from geninst import decode_instruction
from update_PC import update_PC

archi=32  # architecture 32 bits
nb_reg=32 # nombre de registre du banc de registres

# La mémoire est modélisée comme une liste de mot de 8b
# mem = [b'11001000', b'10000110', b'00001010', b'00000000',
#        b'11001001', b'10000110', b'00000100', b'00000000',
#        b'11001101', b'00000000', b'10001100', b'00000000']
mem = []

def mem_gen():
    rd=1
    rs1=0
    rs2=0
    val=0xAAA

    for op in  ['addi', 'xori', 'ori', 'andi',
                'slli', 'srli', 'srai', 'slti', 'sltiu']:

        inst= GenInst.parse_instruction(f"{op} {rd},{rs1},{val}")
        rd = (rd + 1) % 32
        rs1 = rd - 1
        val = val + 1
        yield inst

    yield GenInst.parse_instruction(f"xori {rd},{rs1},{val}")
    rd = (rd + 1) % 32
    rs1 = rd - 1
    val = val + 1
    yield GenInst.parse_instruction(f"xori {rd},{rs1},{val}")
    rd = (rd + 1) % 32
    rs1 = rd - 1
    val = val + 1

    for op in  ['add', 'sub', 'xor', 'or', 'and',
                'sll', 'srl', 'sra', 'slt', 'sltu']:
        rs1 = rd - 2
        rs2 = rd - 1

        inst= GenInst.parse_instruction(f"{op} {rd},{rs1},{rs2}")
        rd = (rd + 1) % 32
        yield inst

    rd = 3
    for op in ['beq', 'bne', 'blt', 'bge', 'bltu', 'bgeu']:
        rs1 = rd - 2
        rs2 = rd - 1

        val = 4
        inst= GenInst.parse_instruction(f"{op} {rs1},{rs2},{val}")
        rd = (rd + 1) % 32
        yield inst

    yield GenInst.parse_instruction(f"jal 22,4")
    yield GenInst.parse_instruction(f"jalr 23,22,4")
    yield GenInst.parse_instruction(f"lui 24,{0xAAAAA}")
    yield GenInst.parse_instruction(f"auipc 25,{0xF0000}")

def init_mem(prog=None):
    addr=0

    if prog is None :
        for i in mem_gen():
            mem.append(i[0:8])
            mem.append(i[8:16])
            mem.append(i[16:24])
            mem.append(i[24:32])
    else:
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
    if opcode  in [b'1100110', b'1100100', b'1100011', b'1110011']:
        return banc[decodeur.rs1.to_uint()]
    elif opcode in [b'1110100']:
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

def exec_alu(opcode, op, x, y):
    if opcode in [b'1100110', b'1100100', b'1100011', b'1110110', b'1110100', b'1110011']:
        # opération arithmétique, avec immédiat, branchement conditionnel, lui, auipc, jalr
        try:
            alu.eval(op, x, y)
        except Exception as e:
            print(f"X = {decodeur.rs1.to_uint()}")
            print(f"Y = {decodeur.rs2.to_uint()}")
            print(banc)
            raise e

def writeback(opcode, funct3):
    # mise à jour banc de registres
    if opcode in [b'1100110', b'1100100']:
        if funct3.to_bytes() == b'010':
            return BitArray(alu.sign and not alu.overflow, archi)
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
    # Écrit l'instruction à l'adresse PC dans IR
    IR.ecriture(fetch(PC.lecture()))
    print(f"Execution de {decode_instruction(IR.lecture())}")

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

        exec_alu(opcode, decodeur.alu_op, x, y)

    ############## Write Back ################################
    if opcode not in [b'1100011']:
        banc[decodeur.rd.to_uint()] = writeback(opcode, decodeur.funct3)

    # Mise à jour de PC
    PC.ecriture(update_PC(decodeur, PC.lecture(), alu))

fibo = ['addi 1,0,10', # n <- 10
        'addi 2,0,2',  # i <- 2
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
