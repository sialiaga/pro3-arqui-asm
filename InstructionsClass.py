from dataclasses import replace
from os.path import exists
import re
import defs

class InstructionsClass:
    def __init__(self, _fileDir=False):
        self.fileDir = ""
        if _fileDir != False: self.setFile(_fileDir)
        
        self.intructions_line = {}
        self.jumps = {}
        self.fileRead = False
        self.numLines = 0
        self.starCode = 0
    
    def checkFile(self, _fileDir):
        #check if file exist
        if (exists(_fileDir)):
            self.fileRead = False
            self.fileDir = _fileDir
        else:
            raise Exception("File not found")
    
    def obtainInstructions(self):
        if self.fileRead == True: return
        self.fileRead = True

        code_start = False
        count_line = 1
        aux_line = ""
        path_line = re.compile(r'([a-zA-Z]{2,4}) (.*)')

        cln = lambda line:line.replace("\n", "")

        file = open(self.fileDir, "r")

        for line in file:
            if code_start == True:
                if cln(line)[-1:] == ":":
                    self.intructions_line[count_line] = {"type":"POS"}
                    self.jumps[cln(line)[:-1]] = count_line
                else:
                    aux_line = cln(line)
                    if aux_line[0:2] == "  ": aux_line[2:]
                    aux_line = path_line.search(aux_line)
                    if defs.in_labels(aux_line.group(1)): self.intructions_line[count_line] = {"type":aux_line.group(1), "args":aux_line.group(2)}
                    else: self.intructions_line[count_line] = {"type":"ERR", "error":aux_line.group(1)}
                count_line += 1
            elif cln(line) == "CODE:":
                code_start = True
                self.starCode = count_line + 1
                count_line = 0
            
            if code_start == False: count_line += 1

        self.numLines = count_line


        #check instructions
    
    def setFile(self, _fileDir):
        self.checkFile(_fileDir)

    def getFile(self):
        return self.fileDir
    
    def getStarCode(self):
        self.obtainInstructions()
        return self.starCode

    def getNumLines(self):
        self.obtainInstructions()
        return self.numLines

    def getAllInstructions(self):
        self.obtainInstructions()
        return self.intructions_line
    
    def getAllJumps(self):
        self.obtainInstructions()
        return self.jumps

    def getInstruction(self, num_line):
        self.obtainInstructions()
        return self.intructions_line[num_line]

    def getJump(self, label):
        self.obtainInstructions()
        return self.jumps[label]


    
