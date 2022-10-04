for i in range(Instructions.getNumLines()):
    print(i+Instructions.getStarCode(), Instructions.getInstruction(i))
print(list(errorline+Instructions.getStarCode() for errorline in Instructions.getPosError()))