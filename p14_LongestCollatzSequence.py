import time
from math import sqrt, log
from collections import defaultdict

#Get all prime factors and use formula till we find the number:
print("Formula and all prime factors:")

m1_start_time = time.time()
max_check = 1000000
max_count = 0
start_max = 0
records = {}

def CollatzLength(start, num, count = 1):
	if num == 1:
		records[start] = count
		return count

	if num in records:
		records[start] = records[num] + count - 1
		return records[num] + count - 1
	elif num % 2 == 0:
		return CollatzLength(start, num/2, count + 1)
	else:
		return CollatzLength(start, ((3 * num) + 1), count + 1)

for i in range(1, max_check + 1):
	current_count = CollatzLength(i, i)

	if current_count > max_count:
		max_count = current_count
		start_max = i

print("Answer: " + str(start_max) + "; Time: " + str(time.time() - m1_start_time))