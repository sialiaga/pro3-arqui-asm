#Imports
from ast import Break
from pickle import TRUE
from re import M
from InstructionsClass import *
from MemoryClass import *
import os



#Objets

file = input("ingrese archivo: ")
Instructions = InstructionsClass(file)
Memory = MemoryClass(file)

file_name = (file.split("/")[-1:])[0].split(".")[0]

while True:
    Memory.obtainMemory()
    for i in Memory.getPosError():
        aux = Memory.getMemory(i)
        print("DATA -",aux['name'], ": ", aux["type"], " ", aux["case"])

    Instructions.obtainInstructions()
    for i in Instructions.getPosError():
        aux = Instructions.getInstruction(i)
        print("CODE -", aux["type"], ": ", aux["error"], "- line:", i)

    if len(Instructions.getPosError()) == 0 and len(Memory.getPosError()) == 0: print("Not errors founded")
    else: break
    
    print(Memory.export(file_name))
    print(Instructions.export(file_name))
    break

open("./temp/memory.log", "w").close()
open("./temp/jumps.log", "w").close()

