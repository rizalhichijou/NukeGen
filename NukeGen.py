import random


min = 1000000
max = 300000
file = open("code.txt","a")
for i in range(0,99):
 va = random.randrange( min - max + 1 * max )
 print "Code is : "+str( va )
 file.write(str(va)+"\n")
