#Imports
from InstructionsClass import *
from MemoryClass import *
from refileClass import *
from os.path import exists


while True: # First, I know... is a horrible practice, but Only use to continue or abort in the error cases
    file = input("ingrese archivo: ")
    if (exists(file)): print("INFO: File Found...") #Check if the file founded
    else:
        print("INFO: File not found or exist")
        break

   
    Refile = RefileClass(file) #Modification to can transalate with the code logic
    Refile.checkType() #check if file have CODE and DATA labels
    Refile.extractLines() #Obtain lineas anh use filters to clean and fix
    Refile.exportRefile() #Make a file to read

    Instructions = InstructionsClass("./temp/refile.ass")
    Memory = MemoryClass("./temp/refile.ass")

    file_name = (file.split("/")[-1:])[0].split(".")[0] #Label to use to name in result files

    print("INFO: Read file...")
    Memory.obtainMemory() # read and translate lines of data
    for i in Memory.getPosError(): #Show Errors
        aux = Memory.getMemory(i)
        print("DATA -",aux['name'], ": ", aux["type"], " ", aux["case"])

    Instructions.obtainJump() #Auxiliar fuction to write file and use in multiples programs
    Instructions.obtainInstructions() # read and translate lines of code
    for i in Instructions.getPosError(): #Show Errors
        aux = Instructions.getInstruction(i)
        print("CODE -", aux["type"], ": ", aux["error"], "- line:", i)
    
    if len(Instructions.getPosError()) == 0 and len(Memory.getPosError()) == 0: print("INFO: Not errors founded - Files make now ") #Check if not exist error
    else: 
        print("INFO: Errors founded - Impossible make files ")
        break
    print("INFO: translate file...")
    print(Memory.export(file_name)) #Create .mem
    print(Instructions.export(file_name)) #Create .out
    break

if True: #Change (True) to (False) if you want see the auxiliar files
    open("./temp/memory.log", "w").close()
    open("./temp/jumps.log", "w").close()
    open("./temp/refile.ass", "w").close()

