import re

class RefileClass:
    #constructor
    def __init__(self, _fileDir):
        self.fileDir = _fileDir
        self.dataFile = []
        self.notdata = ["\n", "#", "b", ", ", " ,", " , ", "RET", ":"]
        self.newdata = ["", "0x", "0b", ",", ",", ",", "RET 0", ": "]
        self.havecode = False
        self.havedata = False

    def checkType(self):
        file = open(self.fileDir, "r")
        for line in file:
            if "DATA:" in line: self.havedata = True
            if "CODE:" in line: self.havecode = True
    
     #check if file exist
    def extractLines(self):
        if self.havedata == False and self.havecode == False: self.dataFile.append("CODE:")
        path = re.compile(r" *?[a-zA-Z].*")
        file = open(self.fileDir, "r")
        for line in file:
            aux_line = line
            for repl in range(len(self.notdata)):
                aux_line = aux_line.replace(self.notdata[repl], self.newdata[repl])
            if (":" in aux_line) and (len(aux_line.split(":")) == 2):
                aux_line = aux_line.split(":") 
                self.dataFile.append(f"{aux_line[0]}:")
                if path.match(aux_line[1]) != None:
                    self.dataFile.append(aux_line[1])

            else:
                self.dataFile.append(aux_line)
        if self.havedata == True and self.havecode == False: self.dataFile.append("CODE:")
    
    def exportRefile(self):
        refile = open("./temp/refile.ass", "w")
        for line in self.dataFile:
            refile.write(line+"\n")
        refile.close()

    def getLines(self):
        return self.dataFile


    
