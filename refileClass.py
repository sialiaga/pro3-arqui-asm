from os.path import exists
import defs as d

class InstructionsClass:
    #constructor
    def __init__(self, _fileDir=False):
        self.fileDir = ""
        if _fileDir != False: self.setFile(_fileDir)
        
        self.intructions_line = {}
        self.jumps = {}
        self.fileRead = False
        
        self.numLines = 0
        self.starCode = 0
        self.posErrors = []
        
        open("./temp/jumps.log", "w").close()
    
     #check if file exist
    def checkFile(self, _fileDir):
        if self.fileRead == True: return
        
        if (exists(_fileDir)): #File exist
            self.fileRead = False
            self.intructions_line = {}
            self.jumps = {}
            self.posErrors = []
            self.fileDir = _fileDir
            return 0
        else: #file not exist
            print("\"",_fileDir, "\" File not found")
            return -1
    
    def obtainJump(self):

        code_start = False
        count_line = 0
        aux_line = ""

        cln = lambda line:line.replace("\n", "")

        file = open(self.fileDir, "r")
        
        for line in file:
            if code_start == True: # "CODE:" was found
                
                if cln(line)[-1:] == ":": #Jump Position
                    jw = open("./temp/jumps.log", "a")
                    jw.write(f"{cln(line)[:-1]};{count_line}\n")
                    jw.close()
                
                else: #Instruction line
                    count_line += 1
            
            elif cln(line) == "CODE:": #now code start is found, to after 
                code_start = True

        self.numLines = count_line

    #obtain and check if instructions is correct
    def obtainInstructions(self):
        if self.fileRead == True: return
        if self.checkFile(self.fileDir) == -1: return
        self.fileRead = True

        code_start = False
        count_line = 1
        aux_line = ""

        cln = lambda line:line.replace("\n", "")

        self.obtainJump()

        file = open(self.fileDir, "r")

        for line in file:
            if code_start == True: # "CODE:" was found
                if cln(line)[-1:] != ":": #Skip Jump Position
                    aux_line = "" #Aux line to clean
                    read_line = 0
                    for c in cln(line):
                        if c != " " and read_line == 0:
                            read_line = 1
                        if read_line == 1:
                            aux_line += c
                    
                    re_result = d.check_intru(aux_line)
                    if re_result[0] == 1:
                        self.intructions_line[count_line] = {"type":re_result[1], "arg":re_result[2], "opcode":re_result[3], "lit":re_result[4]}
                    else:
                        self.intructions_line[count_line] = {"type":"ERR", "error":re_result[1], "conflict":re_result[2]}
                        self.posErrors.append(count_line)
                    
                    count_line += 1
            
            elif cln(line) == "CODE:": #now code start is found, to after read the instructions lines
                code_start = True
                self.starCode = count_line
                count_line = 0
            
            #use to count lines in the start of the file
            if code_start == False: 
                count_line += 1

        self.numLines = count_line
    
    def export(self, name_file_to_export):
        if self.checkFile(self.fileDir) == -1: return "ERR :  Presencia de errores - Imposible crear .out"
        self.obtainInstructions()
        if len(self.posErrors) != 0: return "ERR :  Presencia de errores - Imposible crear .out"
        w = open("./out/"+name_file_to_export+"_out.out", "w")
        for intru in self.intructions_line:
            w.write(self.intructions_line[intru]['opcode']+self.intructions_line[intru]['lit']+"\n")
        w.close()
        return "INFO: Archivo .out creado con exito"

    #redefine file directory
    def setFile(self, _fileDir):
        return self.checkFile(_fileDir)

    #obtain file directory
    def getFile(self):
        return self.fileDir
    
    #return position of the file where code start
    def getStarCode(self):
        self.obtainInstructions()
        return self.starCode

    #return numbers lines of the file
    def getNumLines(self):
        self.obtainInstructions()
        return self.numLines

    #return dictionary with all instructions
    def getAllInstructions(self):
        self.obtainInstructions()
        return self.intructions_line
    
    #return dictionary with jumps and position in instrcution dictionary
    def getAllJumps(self):
        self.obtainInstructions()
        return self.jumps

    #return instruction in line "num_line" passed
    def getInstruction(self, num_line):
        self.obtainInstructions()
        return self.intructions_line[num_line]

    #return postion of label jump passed
    def getJump(self, label):
        self.obtainInstructions()
        return self.jumps[label]

    def getPosError(self):
        self.obtainInstructions()
        if self.checkFile(self.fileDir) == -1: return
        return self.posErrors


    
