import re
label_DATA = {  "MOV":{"re":r"(A),(B)|(B),(A)|([A|B]),(\([A-Za-z]+\))|(\([^A][^B][A-Za-z]+\)),([A|B])|(\([^A][A-Za-z]+\)),([A])|([A|B]),([0-9]+)"},
                "ADD":{"re":r"((A),(B))|(B),(A)|(A),(\([^A][A-Za-z]*\))|((B),(\([^B][A-Za-z]*\)))|(\([^B][^A][A-Za-z]+\))|(([A|B]),([0-9]+))"},
                "SUB":{"re":r"((A),(B))|(B),(A)|(A),(\([^A][A-Za-z]*\))|((B),(\([^B][A-Za-z]*\)))|(\([^B][^A][A-Za-z]+\))|(([A|B]),([0-9]+))" },
                "AND":{"re":r"((A),(B))|(B),(A)|(A),(\([^A][A-Za-z]*\))|((B),(\([^B][A-Za-z]*\)))|(\([^B][^A][A-Za-z]+\))|(([A|B]),([0-9]+))"},
                "OR":{"re":r"((A),(B))|(B),(A)|(A),(\([A-Za-z]*\))|((B),(\([^B][A-Za-z]*\)))|(\([^B][A-Za-z]+\))|(([A|B]),([0-9]+))"},
                "NOT":{"re":r"((A|B),(A|B))|(\([A-Za-z]+\)),(A|B)|(\([B]\))"},
                "XOR":{"re":r"((A),(B))|(B),(A)|(A),(\([^A][A-Za-z]*\))|((B),(\([^B][A-Za-z]*\)))|(\([^B][^A][A-Za-z]+\))|(([A|B]),([0-9]+))"},
                "SHL":{"re":r"((A|B),(A|B))|(\([A-Za-z]+\)),(A|B)|(\([B]\))"},
                "SHR":{"re":r"((A|B),(A|B))|(\([A-Za-z]+\)),(A|B)|(\([B]\))"},
                "INC":{"re":r"(\([^A][A-Za-z]+\))|\(?[B]\)?"},
                "RST":{"re":r"(\([^A][A-Za-z]+\))"},
                "CMP":{"re":r"((A),(B))|(A),(\([A-Za-z]*\))|((B),(\([^B][A-Za-z]*\)))|(\([^B][A-Za-z]+\))|(([A|B]),([0-9]+))"},
                "CALL":{"re":r"\w*"},
                "RET":{"re":r".*"},
                "PUSH":{"re":r"[A|B]"},
                "POP":{"re":r"[A|B]"},
                "JMP":{"re":r"\w*"},
                "JEQ":{"re":r"\w*"},
                "JNE":{"re":r"\w*"},
                "JGT":{"re":r"\w*"},
                "JLT":{"re":r"\w*"},
                "JGE":{"re":r"\w*"},
                "JLE":{"re":r"\w*"},
                "JCR":{"re":r"\w*"},
                "JOV":{"re":r"\w*"}}

def in_labels(label):
    if label in label_DATA: return True
    else: return False

def get_re(label):
    return label_DATA[label]["re"]