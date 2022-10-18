#Imports
from re import M
from InstructionsClass import *
from MemoryClass import *
import os



#Objets

file = input("ingrese archivo: ")
Instructions = InstructionsClass(file)
Memory = MemoryClass()


# if Memory.setFile(file) != -1:
#     print(Memory.getAllMemory())
#     print(Memory.getPosError())
#     print(Memory.getSizeData)

Instructions.obtainInstructions()

for i in Instructions.getPosError():
    aux = Instructions.getInstruction(i)
    print(aux["type"], ": ", aux["error"], " ", aux["conflict"], "- line:", i+Instructions.getStarCode())

if len(Instructions.getPosError()) == 0: print("Not errors founded")


for i in range(Instructions.getNumLines()):
    print(i, Instructions.getInstruction(i))

print(Instructions.export("instructions"))



