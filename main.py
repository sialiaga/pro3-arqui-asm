#Imports
from InstructionsClass import *
import os

#Objets
Instructions = InstructionsClass()
file = input("ingrese archivo: ")
aux = ""
Instructions.setFile(file)

for i in Instructions.getPosError():
    aux = Instructions.getInstruction(i)
    print(aux["type"], ": ", aux["error"], " ", aux["error_val"])

# aux = input("dir:")

# Instructions.setFile(aux)
# for i in range(Instructions.getNumLines()):
#     print(i+Instructions.getStarCode(), Instructions.getInstruction(i))
# print(Instructions.getCountError())


