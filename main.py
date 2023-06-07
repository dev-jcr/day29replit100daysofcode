# arguments end and sep inside print
import os, time

def newPrint(color, word):
  if color =="red":
    print("\033[31m", word, sep="", end="")
  elif color=="purple":
    print("\033[1;35m", word, sep="", end="")
  elif color =="cyan":
    print("\033[0;36m", word, sep="", end="")
  else:
    print("\033[0m", word, sep="", end="")
    
print("Super subroutine\n")
print("With my " , end="")
newPrint("purple","new program")
newPrint("reset", " I can just call red(\"and\") ")
newPrint("red", "it will print in red ")
newPrint("cyan", "or even cyan.\n\n")
newPrint("reset","With no")
newPrint("cyan", " weird gaps")
