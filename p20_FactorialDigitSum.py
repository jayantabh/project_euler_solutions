import time
import datetime

#Direct Loop:
print("Direct Loop:")

m1_start_time = time.time()
max_check = 100
factorial = 1
sum = 0

for i in range(1,max_check + 1):
	factorial *= i

str_factorial = str(factorial)

for digit in str_factorial:
	sum += int(digit)

print("Answer: " + str(sum) + "; Time: " + str(time.time() - m1_start_time))