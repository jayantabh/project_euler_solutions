import time
from math import sqrt, log
from collections import defaultdict

#Direct Loop
print("Direct Loop:")

m1_start_time = time.time()
max_check = 100
sum_of_sqaures = 0
sum = 0

for i in range(1, max_check + 1):
	sum = sum + i
	sum_of_sqaures = sum_of_sqaures + i ** 2

square_of_sum = sum ** 2

print("Answer: " + str(square_of_sum - sum_of_sqaures) + "; Time: " + str(time.time() - m1_start_time))

#Formulae
print("Formulae:")

m1_start_time = time.time()
sum_of_sqaures = max_check * (max_check + 1) * ((2 * max_check) + 1) / 6
square_of_sum = (max_check * (max_check + 1)/2) ** 2

print("Answer: " + str(square_of_sum - sum_of_sqaures) + "; Time: " + str(time.time() - m1_start_time))

