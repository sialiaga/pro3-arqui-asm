label_DATA = {  "MOV":{"vn":2},
                "ADD":{"vn":2},
                "SUB":{"vn":2},
                "AND":{"vn":2},
                "OR":{"vn":2},
                "OR":{"vn":2},
                "NOT":{"vn":2},
                "XOR":{"vn":2},
                "SHL":{"vn":2},
                "SHR":{"vn":2},
                "INC":{"vn":1},
                "RST":{"vn":1},
                "CMP":{"vn":2},
                "ADD":{"vn":2},
                "CALL":{"vn":1},
                "RET":{"vn":0},
                "PUSH":{"vn":1},
                "POP":{"vn":1},
                "JMP":{"vn":1},
                "JEQ":{"vn":1},
                "JNE":{"vn":1},
                "JGT":{"vn":1},
                "JLT":{"vn":1},
                "JGE":{"vn":1},
                "JLE":{"vn":1},
                "JCR":{"vn":1},
                "JOV":{"vn":1}}

def in_labels(label):
    if label in label_DATA: return True
    else: return False