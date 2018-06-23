import time
from math import sqrt, log
from collections import defaultdict

#Recursive Memoization:
print("Recursive Memoization:")

m1_start_time = time.time()
names = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}

def CollatzLength(start, num, count = 1):

print("Answer: " + str(start_max) + "; Time: " + str(time.time() - m1_start_time))