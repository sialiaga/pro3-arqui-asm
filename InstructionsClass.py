from dataclasses import replace
from os.path import exists
import re
import defs

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
        self.countErrors = 0
    
     #check if file exist
    def checkFile(self, _fileDir):
        
        if (exists(_fileDir)): #File exist
            self.fileRead = False
            self.intructions_line = {}
            self.jumps = {}
            self.countErrors = 0
            self.fileDir = _fileDir
            return 0
        else: #file not exist
            print("\"",_fileDir, "\" File not found")
            return -1
    
    #obtain and check if instructions is correct
    def obtainInstructions(self):
        if self.fileRead == True: return
        if self.checkFile(self.fileDir) == -1: return
        self.fileRead = True

        code_start = False
        count_line = 1
        aux_line = ""
        path_line = re.compile(r'([a-zA-Z]{2,4}) (.*)')

        cln = lambda line:line.replace("\n", "")

        file = open(self.fileDir, "r")

        for line in file:
            if code_start == True: # "CODE:" was found
                
                if cln(line)[-1:] == ":": #Jump Position
                    self.intructions_line[count_line] = {"type":"POS"}
                    self.jumps[cln(line)[:-1]] = count_line
                
                else: #Instruction line
                    aux_line = cln(line) #Aux line to clean
                    
                    #check if line have a tab
                    if aux_line[0:2] == "  ": #remove tab
                        aux_line[2:]
                    
                    #-re"" to search <instruction> <arguments>
                    aux_line = path_line.search(aux_line) 
                    
                    #check if instruction exist
                    if defs.in_labels(aux_line.group(1)): #line is correct
                        self.__obtainArguments(count_line, aux_line.group(1), aux_line.group(2))
                    
                    else: #line with error
                        self.intructions_line[count_line] = {"type":"ERR", "error":"not found instruction", "error_val":aux_line.group(1)}
                        self.countErrors += 1
                
                count_line += 1
            
            elif cln(line) == "CODE:": #now code start is found, to after read the instructions lines
                code_start = True
                self.starCode = count_line + 1
                count_line = 0
            
            #use to count lines in the start of the file
            if code_start == False: 
                count_line += 1

        self.numLines = count_line

    def __obtainArguments(self, line, instruction, arguments):
        path = re.compile(defs.get_re(instruction))
        print(path.match(arguments))
        if path.match(arguments) != None and arguments[-1:] != ",":
            self.intructions_line[line] = {"type":instruction, "args":arguments.split(",")}
        else:
            self.intructions_line[line] = {"type":"ERR", "error":"invalid arguments", "error_val":arguments}
        
        
    #redefine file directory
    def setFile(self, _fileDir):
        self.checkFile(_fileDir)

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

    def getCountError(self):
        self.obtainInstructions()
        return self.countErrors


    
