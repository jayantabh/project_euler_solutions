import time
from math import log

#Direct Loop:
print("Direct Loop:")

m1_start_time = time.time()

max_check = 1000
max_count = 0
max_number = 0

for i in range(1, max_check):
	numbers = {}
	remainder = 0
	position = 1
	numerator = 10
	perfect_division_flag = 0
	while(numerator not in numbers):
		if numerator >= i:
			remainder = numerator % i
			numbers[numerator] = position
			if remainder == 0:
				perfect_division_flag = 1
				# print(str(i) + ": Perfect Division")
				break
			numerator = remainder
		else:
			numerator *= 10
		position += 1

	if perfect_division_flag == 0  and max_count < (position - numbers[numerator]):
		max_count = position - numbers[numerator]
		max_number = i

print("Answer: " + str(max_number) + "; Time: " + str(time.time() - m1_start_time))