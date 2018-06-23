import time
from math import sqrt, log
from collections import defaultdict

#Direct Loop:
print("Direct Loop:")

m1_start_time = time.time()
num = 2
power = 1000

def SumOfDigits(num, power):
	n = num ** power
	sum = 0
	i = 1
	while(n>0):
		sum = sum + (n % 10)
		n = n // 10
		i = i + 1

	return sum

print("Answer: " + str(SumOfDigits(2,1000000)) + "; Time: " + str(time.time() - m1_start_time))

#Direct Loop with String:
print("Direct Loop with String:")

m2_start_time = time.time()
num = 2
power = 1000

def SumOfDigits(num, power):
	sum = 0
	for s in str(num ** power):
		sum = sum + int(s)

	return sum

print("Answer: " + str(SumOfDigits(2,1000000)) + "; Time: " + str(time.time() - m2_start_time))