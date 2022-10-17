CODE:
    MOV A,B
    ADD A,12
    JMP siguiente
    ADD A,0b0101
siguiente:
    ADD A,0x0aa
    MOV B,A
    JMP juan
juan:
    JMP 05
    MOV (0b010),A
    JMP juan
    CALL juan