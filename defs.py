import re

def translate(argument, opcode): #Argument is translate a 8bit value in lit or dir case
    aux_value = "00000000" #main value, persist in the case that opcode not in lit or dir opcode cases

    notFoundLabel = 1
    notFoundMemory = 1

    overflow = lambda value : 0 if value<256 else 1 #check overflow
    overflow_c2 = lambda value : 0 if value<128 else 1 #check overflow in c'2 case
    bin8coverter = lambda value :"0"*(8-len(value)) + value #transform binary diferente of 8bit to a 8bit binary

    #Thanks to user AJP in https://www.kutombawewe.net/es/python/complemento-binario-de-dos-en-python/1069168616/amp/
    c2binary = lambda x, count=8: "".join(map(lambda y:str((x>>y)&1), range(count-1, -1, -1)))  #Use to pass negative value to c'2 value

    data = open("./dat/opcodespecial.dat", "r") #Only need know if the opcode use a lit to translate this lit
    for spec in data:
        aux_spec = spec.replace("\n", "").split(";")
        if (opcode == aux_spec[1] and "lit"==aux_spec[0]) or opcode == "mem":
            for args in argument:
                aux_arg = args.replace("(", "").replace(")", "")
                #Hex Case
                if aux_arg[:2] == "0x":
                    if overflow(int(aux_arg, 16)): return [0, aux_arg, "Overflow Literal"]
                    aux_value = int(aux_arg, 16)
                    aux_value = str(bin(aux_value))[2:]
                    aux_value = bin8coverter(aux_value)
                    return [1, aux_value]
                #Binary Case
                elif aux_arg[:2] == "0b":
                    if overflow(int(aux_arg, 2)): return [0, aux_arg, "Overflow Literal"]
                    aux_value = aux_arg[2:]
                    aux_value = bin8coverter(aux_value)
                    return [1, aux_value]
                #Decimal Case
                else:
                    try: 
                        aux_value = int(aux_arg)
                        if aux_value < 0:
                            if overflow_c2(abs(aux_value)): return [0, aux_arg, "Overflow Literal"]
                            aux_value = c2binary(int(aux_arg))
                            return [1, aux_value]
                        else:
                            if overflow(aux_value): return [0, aux_arg, "Overflow Literal"]
                            aux_value = str(bin(aux_value))[2:]
                            aux_value = bin8coverter(aux_value)
                            return [1, aux_value]
                    except:
                        pass
    data.close()
    
    #Jump case, use a aux file to obtain the dir of jumps
    data = open("./dat/opcodespecial.dat", "r")
    data_jump = open("./temp/jumps.log", "r")
    for spec in data:
        aux_spec = spec.replace("\n", "").split(";")
        if opcode == aux_spec[1] and "jump"==aux_spec[0]:
            aux_arg = argument[0]
            for jump in data_jump:
                aux_jump = jump.replace("\n", "").split(";")
                if aux_jump[0] == aux_arg:
                    aux_value = str(bin(int(aux_jump[1])))[2:]
                    aux_value = bin8coverter(aux_value)
                    return [1, aux_value]
            return [0, aux_arg, "Label not exist"]
    data.close()
    data_jump.close()

    #Jump case, use a aux file to obtain the dir of data
    data = open("./dat/opcodespecial.dat", "r")
    data_mem = open("./temp/memory.log", "r")
    for spec in data:
        aux_spec = spec.replace("\n", "").split(";")
        if opcode == aux_spec[1] and "memory"==aux_spec[0]:
            for mem in data_mem:
                aux_mem = mem.replace("\n", "").split(";")
                for args in argument:
                    aux_arg = args.replace("(", "").replace(")", "")
                    if aux_mem[0]==aux_arg:
                        return [1, bin8coverter(str(bin(int(aux_mem[1])))[2:])]
            
            return [0, aux_arg, "Label not exist"]
    data.close()
    data_jump.close()

    #case of not pass lit
    return [1, aux_value]

#Check if instructions is correct
def check_intru(sent):
    data = open("./dat/instructions.dat", "r") #open list of re to check if instruction is correct 
    for seq in data:
        aux_seq = seq.replace("\n", "").split(";")
        path = re.compile(aux_seq[0])
        aux_match = path.match(sent)
        aux_lit = 0
        if aux_match != None and aux_match.group() == sent:
            aux_group = aux_match.group().split(" ")
            aux_group[1] = aux_group[1].split(",")
            aux_lit = translate(aux_group[1],aux_seq[1])
            if aux_lit[0] == 1:
                return [1, aux_group[0], aux_group[1], aux_seq[1], aux_lit[1]]
            else:
                return [0, aux_lit[2], aux_lit[1]]
    data.close()
    data = open("./dat/allinstrus.dat", "r")
    for intru in data: #check type of error
        aux_sent = sent.split(" ")
        if aux_sent[0] == intru.replace("\n", ""):
            return [0, "argument error", aux_sent[1]]
    return [0, "instruction error", sent.split(" ")[0]]

    

        

if __name__ == "__main__":
    i1 = {'type': 'MOV', 'arg': ['A', 'B'], 'opcode': '0000000'}
    i2 = {'type': 'SUB', 'arg': ['A', '12'], 'opcode': '0001010'}
    i3 = {'type': 'JLE', 'arg': ['#0x0a'], 'opcode': '1011001'}
    i4 = {'type': 'CMP', 'arg': ['A', '0b01'], 'opcode': '1001110'}
    i5 = {'type': 'MOV', 'arg': ['A', "(#12)"], 'opcode': '0100101'}
    print(translate(i5))