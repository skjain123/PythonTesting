import math
import random

intcount = int(input("How Many do you numbers are you going to input? "))
x = 0
count = 0
while (count < intcount):
   intnum = int(input("What Number? "))
   count = count + 1
   x = x + intnum

print(x/intcount)
