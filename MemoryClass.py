from os.path import exists
import defs as d
import re

class MemoryClass:
    #constructor
    def __init__(self, _fileDir):
        self.fileDir = _fileDir
        
        self.memories = {}
        self.posErrors = []
        self.fileRead = False
        
        
        open("./temp/memory.log", "w").close()
    

    #obtain and check if Memory is correct
    def obtainMemory(self):
        count_data = 0
        code_start =  False
        aux_line = ""

        re_case = [r"[A-Za-z]{1,} 0b[01]{1,}", r"[A-Za-z]{1,} 0x[0-9a-fA-F]{1,}",r"[A-Za-z]{1,} \d{1,}"]

        cln = lambda line:line.replace("\n", "")

        file = open(self.fileDir, "r")
        mw = open("./temp/memory.log", "a")

        for line in file:
            if cln(line) == "CODE:": #Star Code need end
                break
            
            elif code_start == True: # "Code:" was found
                aux_line = "" 
                read_line = 0
                for c in cln(line):
                    if c != " " and read_line == 0:
                        read_line = 1
                    if read_line == 1:
                        aux_line += c
                self.memories[count_data] = {"name":"ERR","case":aux_line.split(" ")[0], "type":"Estructura incorrecta"}
                self.posErrors.append(count_data)
                for rec in re_case:
                    path = re.compile(rec)
                    aux_match = path.match(aux_line)
                    if aux_match != None and aux_match.group() == aux_line:
                        aux_value = d.translate([aux_line.split(" ")[1]],"mem")
                        if aux_value[0]:
                            self.memories[count_data] = {"name":aux_line.split(" ")[0], "value":aux_value[1]}
                            mw = open("./temp/memory.log", "a")
                            aux_fstring = aux_line.split(" ")[0]
                            mw.write(f"{aux_fstring};{count_data}\n")
                            mw.close()
                            self.posErrors.pop(self.posErrors.index(count_data))
                        else:
                            self.memories[count_data] = {"name":"ERR","case":aux_line.split(" ")[1],"type":aux_value[2]}
                count_data += 1
            
            elif cln(line) == "DATA:": #now code data is found, to after read the instructions lines
                code_start = True
                count_data = 0
    
    #export .mem
    def export(self, name_file_to_export):
        w = open("./out/"+name_file_to_export+"_mem.mem", "w")
        for mem in self.memories:
            w.write(self.memories[mem]["value"]+"\n")
        w = open("./out/"+name_file_to_export+"_mem.mem", "w")
        return "INFO: Archivo .mem creado con exito"
        
    #Obtain all data of memories
    def getAllMemory(self):
        return self.memories

    #obtain one pos of memory
    def getMemory(self, num_mem):
        return self.memories[num_mem]

    #return errors position
    def getPosError(self):
        return self.posErrors


    
