from bitArray import BitArray

def update_PC(decodeur, pc, alu, archi=32):
    """update_PC renvoie la future valeur de PC en fonction de
    l'instruction courante, de la valeur courante de PC et des sorties
    de l'ALU
    """
    opcode = decodeur.opcode.to_bytes()

