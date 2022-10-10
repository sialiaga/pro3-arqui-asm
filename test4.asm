CODE:
    MOV A,B
    ADD A,12
    ADD A,0b0101
    ADD A,0x0aa
    MOV B,A
    JMP #05
    MOV (#0b010),A
