import time
from math import sqrt, log
from collections import defaultdict

#DP - Memoization:
print("DP - Memoization:")

m1_start_time = time.time()
rows = []
with open('/home/jayantabhowmick/workspace/projecteuler/files/p067_triangle.txt') as file:
	for line in file:
		rows.append(line.replace('\n',''))

# rows = [x.strip for x in content]

array = [0] * len(rows)

for i in range(0,len(rows)):
	array[i] = rows[i].split(' ')
	for j in range(0, len(array[i])):
		array[i][j] = int(array[i][j])

for i in range(len(array) - 2, -1, -1):
	for j in range(0, len(array[i])):
		array[i][j] = max((array[i][j] + array[i+1][j]),(array[i][j] + array[i+1][j+1]))

print("Answer: " + str(array[0][0]) + "; Time: " + str(time.time() - m1_start_time))