#Imports
from InstructionsClass import *
import os

#Objets
Instructions = InstructionsClass("test.txt")

for i in range(Instructions.getNumLines()):
    print(i+Instructions.getStarCode(), Instructions.getInstruction(i))

