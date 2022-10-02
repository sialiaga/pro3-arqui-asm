from os.path import exists

class InstructionsClass:
    def __init__(self, _fileDir=False):
        self.fileDir = ""
        self.intructions_line = {}
        self.jumps = {}
        if _fileDir != False: self.setFile(_fileDir)
    
    def checkFile(self, _fileDir):
        if (exists(_fileDir)):
            self.fileDir = _fileDir
        else:
            raise Exception("File not found")
    
    def setFile(self, _fileDir):
        self.checkFile(_fileDir)

    def getFile(self):
        return self.fileDir