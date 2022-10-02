#Imports
from InstructionsClass import *
import os

#Objets
Instructions = InstructionsClass("test.txt")

#Compiler
os.system('cls')
user_input = input("Ingrese dir: ")
Instructions.setFile(user_input)
os.system('cls')
print(Instructions.getFile())

