#Imports
from re import M
from InstructionsClass import *
from MemoryClass import *
import os



#Objets
Instructions = InstructionsClass()
Memory = MemoryClass()
file = input("ingrese archivo: ")

if Memory.setFile(file) != -1:
    print(Memory.getAllMemory())

# if Instructions.setFile(file) != -1:

#     for i in Instructions.getPosError():
#         aux = Instructions.getInstruction(i)
#         print(aux["type"], ": ", aux["error"], " ", aux["conflict"], "- line:", i+Instructions.getStarCode())

#     if len(Instructions.getPosError()) == 0: print("Not errors founded")


#     for i in range(Instructions.getNumLines()):
#         print(i, Instructions.getInstruction(i))

#     print(Instructions.export("instructions"))



