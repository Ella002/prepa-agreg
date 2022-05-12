# Réponses aux questions #

## Question 4 ##

*Trouver les fonctions booléennes sur les flags `carry`, `overflow`, `sign` et `zero` pour `beq`, `bne`, `blt`, `bge`, `bltu` et `bgeu`*

| operation | fonction |
|-----------|----------|
| beq       | ZF       |
| bne       | !ZF      |
| blt       | OF != SF |
| bge       | OF = SF  |
| bltu      | CF       |
| bgeu      | !CF      |

## Question 5 ##

*Table logique pour les sorties d'un additionneur 1 bit à deux opérandes*

| a | b | cin | s | cout |
|---|---|-----|---|------|
| 0 | 0 | 0   | 0 | 0    |
| 0 | 0 | 1   | 1 | 0    |
| 0 | 1 | 0   | 1 | 0    |
| 0 | 1 | 1   | 0 | 1    |
| 1 | 0 | 0   | 1 | 0    |
| 1 | 0 | 1   | 0 | 1    |
| 1 | 1 | 0   | 0 | 1    |
| 1 | 1 | 1   | 1 | 1    |

s = !a & !b & c || !a & b & !c || a & !b & !c || a & b & c
  = a xor b xor c

cout = a & b || a & c || b & c

## Question 6 ##

## Question 9 ##

| instruction | operation       |
|-------------|-----------------|
| add         | add             |
| sub         | sub             |
| xor         | xor             |
| or          | bor             |
| and         | band            |
| slt         | not implemented |
| sltu        | not implemented |
| sll         | sll             |
| srl         | srl             |
| sra         | sra             |
| addi        | add             |
| xori        | xor             |
| ori         | bor             |
| andi        | band            |
| slti        | not implemented |
| sltiu       | not implemented |
| slli        | sll             |
| srli        | srl             |
| srai        | sra             |
| beq         | sub             |
| bne         | sub             |
| blt         | sub             |
| bge         | sub             |
| bltu        | sub             |
| bgeu        | sub             |
| jal         | none            |
| jalr        | none            |
| lui         | sll             |
| auipc       | not implemented |

## Question 10 ##

`jal rd, imm` -> `PC = PC + imm`
`jalr rd, rs1, imm` -> `PC = rs1 + imm`
`b... rs1, rs2, imm` -> si condition sur rs1 et rs2, `PC = PC + imm`
	                      sinon, `PC = PC + 4`
sinon, `PC = PC + 4`
