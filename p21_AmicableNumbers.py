import time
from math import sqrt

#Direct Loop through all possible:
print("Direct Loop through all possible:")

m1_start_time = time.time()

max_check = 10000

def GetProperDivisors(n) :
    divisors = [1] 
    for i in range(2, int(sqrt(n) + 1)) :
        if (n % i == 0) :
            if (n / i == i) :
                divisors.append(i)
            else :
                divisors.extend((i, int(n/i)))
    return divisors

number_divisor_sum = [0] * (max_check + 1)

amicable_numbers = [0] * (max_check + 1)

sum_of_divisors = 0

for i in range(1, max_check + 1):
	sum_of_divisors = sum(GetProperDivisors(i))
	number_divisor_sum[i] = sum_of_divisors
	for x in range(1, i):
		if (i == number_divisor_sum[x]) and (number_divisor_sum[i] == x):
			amicable_numbers[x] = 1
			amicable_numbers[i] = 1  
			# print(x, i, number_divisor_sum[x], number_divisor_sum[i]) 
total = 0

for x in range(0, max_check + 1):
	if amicable_numbers[x] == 1:
		total += x

print("Answer: " + str(total) + "; Time: " + str(time.time() - m1_start_time))

#Direct Loop - Only finding reverse of possible:
print("Direct Loop - Only finding reverse of possible:")

m1_start_time = time.time()

max_check = 10000

def GetProperDivisors(n) :
    divisors = [1] 
    for i in range(2, int(sqrt(n) + 1)) :
        if (n % i == 0) :
            if (n / i == i) :
                divisors.append(i)
            else :
                divisors.extend((i, int(n/i)))
    return divisors

amicable_numbers = [0] * (max_check + 1)

sum_of_divisors = 0

for i in range(1, max_check + 1):
	sum_of_divisors = sum(GetProperDivisors(i))
	number_divisor_sum[i] = sum_of_divisors
	if sum_of_divisors > i and i == sum(GetProperDivisors(sum_of_divisors)):
		amicable_numbers[i] = 1
		amicable_numbers[sum_of_divisors] = 1  

total = 0

for x in range(0, max_check + 1):
	if amicable_numbers[x] == 1:
		total += x

print("Answer: " + str(total) + "; Time: " + str(time.time() - m1_start_time))

#Implement using prime factor and formula
