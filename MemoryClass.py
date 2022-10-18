from os.path import exists
import defs as d
import re

class MemoryClass:
    #constructor
    def __init__(self, _fileDir=False):
        self.fileDir = ""
        if _fileDir != False: self.setFile(_fileDir)
        
        self.memories = {}
        self.posErrors = []
        self.fileRead = False
        
        
        open("./temp/memory.log", "w").close()
    
     #check if file exist
    def checkFile(self, _fileDir):
        if self.fileRead == True: return
        
        if (exists(_fileDir)): #File exist
            self.memories = {}
            self.posErrors = []
            self.fileRead = False
            self.fileDir = _fileDir
            return 0
        else: #file not exist
            print("\"",_fileDir, "\" File not founded")
            return -1
    
    #obtain and check if Memory is correct
    def obtainMemory(self):
        if self.fileRead == True: return
        if self.checkFile(self.fileDir) == -1: return
        self.fileRead = True

        count_data = 0
        code_start =  False
        aux_line = ""

        re_case = [r"[A-Za-z]{1,} 0b[01]{1,}", r"[A-Za-z]{1,} 0x[0-9a-fA-F]{1,}",r"[A-Za-z]{1,} \d{1,}"]

        cln = lambda line:line.replace("\n", "")

        file = open(self.fileDir, "r")

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
                            self.posErrors.pop(self.posErrors.index(count_data))
                        else:
                            self.memories[count_data] = {"name":"ERR","case":aux_line.split(" ")[1],"type":aux_value[2]}
                count_data += 1
            
            elif cln(line) == "DATA:": #now code data is found, to after read the instructions lines
                code_start = True
                count_data = 0
    
    def export(self, name_file_to_export):
        if self.checkFile(self.fileDir) == -1: return "ERR :  Presencia de errores - Imposible crear .out"
        self.obtainMemory()
        if len(self.posErrors) != 0: return "ERR :  Presencia de errores - Imposible crear .out"
        w = open("./out/"+name_file_to_export+"_mem.mem", "w")
        

    #redefine file directory
    def setFile(self, _fileDir):
        return self.checkFile(_fileDir)

    #obtain file directory
    def getFile(self):
        return self.fileDir
    
    #return dictionary with all Memories
    def getAllMemory(self):
        self.obtainMemory()
        return self.memories

    #return instruction in line "num_mem" passed
    def getMemory(self, num_mem):
        self.obtainMemory()
        return self.memories[num_mem]

    #return error position
    def getPosError(self):
        self.obtainMemory()
        return self.posErrors


    
