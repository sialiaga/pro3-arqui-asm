import re

def check_intru(sent):
    data = open("instructions.dat", "r")
    for seq in data:
        aux_seq = seq.replace("\n", "").split(";")
        path = re.compile(aux_seq[0])
        aux_match = path.match(sent)
        if aux_match != None and aux_match.group() == sent:
            aux_group = aux_match.group().split(" ")
            return [1, aux_group[0], aux_group[1].split(","), aux_seq[1]]
    data.close()
    data = open("allinstrus.dat", "r")
    for intru in data:
        aux_sent = sent.split(" ")
        if aux_sent[0] == intru.replace("\n", ""):
            return [0, "argument error", aux_sent[1]]
    return [0, "instruction error", sent.split(" ")[0]]

def translate(intru):
    data = open("opcodewlit.dat", "r")
    aux_value = "00000000"
    for wlit in data:
        if intru["opcode"] == wlit.replace("\n", ""):
            for args in intru['arg']:
                aux_arg = args.replace("(", "").replace(")", "").replace("#", "")
                if aux_arg[:2] == "0x":
                    aux_value = int(aux_arg, 16)
                    aux_value = str(bin(aux_value))[2:]
                    aux_value = "0"*(8-len(aux_value)) + aux_value
                elif aux_arg[:2] == "0b":
                    aux_value = aux_arg[2:]
                    aux_value = "0"*(8-len(aux_value)) + aux_value
                else:
                    try:
                        aux_value = str(bin(int(aux_arg)))[2:]
                        aux_value = "0"*(8-len(aux_value)) + aux_value
                    except:
                        pass
    return intru["opcode"] + aux_value

    

        

if __name__ == "__main__":
    i1 = {'type': 'MOV', 'arg': ['A', 'B'], 'opcode': '0000000'}
    i2 = {'type': 'SUB', 'arg': ['A', '12'], 'opcode': '0001010'}
    i3 = {'type': 'JLE', 'arg': ['#0x0a'], 'opcode': '1011001'}
    i4 = {'type': 'CMP', 'arg': ['A', '0b01'], 'opcode': '1001110'}
    i5 = {'type': 'MOV', 'arg': ['A', "(#12)"], 'opcode': '0100101'}
    print(translate(i5))