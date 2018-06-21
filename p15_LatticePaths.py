import time
from math import sqrt, log
from collections import defaultdict

#Recursive Memoization:
print("Recursive Memoization:")

m1_start_time = time.time()
m = 20
n = 20
paths = {}

def LatticePaths1(m, n):
	if (m,n) in paths:
		return paths[(m,n)]
	elif m == 0 or n == 0:
		return 1
	else:
		return LatticePaths1(m - 1, n) + LatticePaths1(m, n - 1)

for i in range(1,m + 1):
	for j in range(1,n + 1):
		if (i,j) not in paths:
			paths[(i,j)] = LatticePaths1(i, j)


print("Answer: " + str(paths[(m,n)]) + "; Time: " + str(time.time() - m1_start_time))

#Recursive Memoization - Part 2:
print("Recursive Memoization - Part 2:")

m2_start_time = time.time()
paths = {}

def LatticePaths2(m, n):
	if (m,n) in paths:
		return paths[(m,n)]
	elif m == 0 or n == 0:
		return 1
	else:
		paths[(m,n)] = LatticePaths2(m - 1, n) + LatticePaths2(m, n - 1)
		return paths[(m,n)]

print("Answer: " + str(LatticePaths2(m,n)) + "; Time: " + str(time.time() - m2_start_time))

#Iterative:
print("Iterative:")

m3_start_time = time.time()

def LatticePaths3(m, n):
	paths = {}

	for i in range(0,m + 1):
		paths[(i,0)] = 1

	for j in range(0,n + 1):
		paths[(0,j)] = 1

	for i in range(1, m + 1):
		for j in range(1, n + 1): 
			paths[(i,j)] = paths[(i-1,j)] + paths[(i, j-1)]

	return paths[(m, n)]

print("Answer: " + str(LatticePaths3(m,n)) + "; Time: " + str(time.time() - m3_start_time))

#Combinatorial:
print("Combinatorial:")

m4_start_time = time.time()

def LatticePaths4(m, n):
	num = 1
	den = 1
	for i in range(m + 1,m + n + 1):
		num = num * i

	for j in range(1, n):
		den = den * j

	return num/den

print("Answer: " + str(LatticePaths4(m, n)) + "; Time: " + str(time.time() - m4_start_time))