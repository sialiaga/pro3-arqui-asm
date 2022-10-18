#Imports
from InstructionsClass import *
from MemoryClass import *
from refileClass import *
from os.path import exists


while True:
    file = input("ingrese archivo: ")
    if (exists(file)): print("INFO: File Found...")
    else:
        print("INFO: File not found or exist")
        break

   
    Refile = RefileClass(file)
    Refile.checkType()
    Refile.extractLines()
    Refile.exportRefile()

    Instructions = InstructionsClass("./temp/refile.ass")
    Memory = MemoryClass("./temp/refile.ass")

    file_name = (file.split("/")[-1:])[0].split(".")[0]
    print("INFO: Read file...")
    Memory.obtainMemory()
    for i in Memory.getPosError():
        aux = Memory.getMemory(i)
        print("DATA -",aux['name'], ": ", aux["type"], " ", aux["case"])

    Instructions.obtainJump()
    Instructions.obtainInstructions()
    for i in Instructions.getPosError():
        aux = Instructions.getInstruction(i)
        print("CODE -", aux["type"], ": ", aux["error"], "- line:", i)
    
    if len(Instructions.getPosError()) == 0 and len(Memory.getPosError()) == 0: print("INFO: Not errors founded - Files make now ")
    else: 
        print("INFO: Errors founded - Impossible make files ")
        break
    print("INFO: translate file...")
    print(Memory.export(file_name))
    print(Instructions.export(file_name))
    break

# open("./temp/memory.log", "w").close()
# open("./temp/jumps.log", "w").close()

