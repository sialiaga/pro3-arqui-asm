#Imports
from InstructionsClass import *
import os

#Objets
Instructions = InstructionsClass()
file = input("ingrese archivo: ")
# aux = ""
Instructions.setFile(file)

for i in Instructions.getPosError():
    aux = Instructions.getInstruction(i)
    print(aux["type"], ": ", aux["error"], " ", aux["error_val"], "- line:", i+Instructions.getStarCode())

if len(Instructions.getPosError()) == 0: print("Not errors founded")

# aux = input("dir:")

# Instructions.setFile(aux)
# for i in range(Instructions.getNumLines()):
#     print(i, Instructions.getInstruction(i))
# print(list(errorline+Instructions.getStarCode() for errorline in Instructions.getPosError()))
print(Instructions.export("intrus_out"))


