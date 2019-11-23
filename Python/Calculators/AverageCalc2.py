from math import *
import random


x = 0
count = 1
intnum = 0

while (count):
   intnum = input("What Number? ")
   if (intnum[0] == "q"):
      break
   else:
      x = x + int(intnum)
      print(x/count)
   count = count + 1
