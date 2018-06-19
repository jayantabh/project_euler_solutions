import time

#Direct Loop
print("Direct Loop Using Mathematical Optimizations:")

m1_start_time = time.time()

num = 600851475143
max = 0
i = 3

#Naive prime test takes lot of time, changed to 
#Primality Tests are not required
# def prime_test(num):
# 	if num <= 1:
# 		return False
# 	elif num <= 3:
# 		return True
# 	elif num % 2 == 0 or num % 3 == 0:
# 		return True
# 	i = 5
# 	while i * i <= num:
# 		if num % i == 0 or num % (i + 2) == 0:
# 			return False
# 		i = i + 6
# 	return True

while num % 2 == 0:
	num = num / 2
	max = 2

while(i * i < num):
	while num % i == 0:
		max = i
		num = num / i
	i = i + 2

if num > 2:
	max = num

print("Answer: " + str(max) + "; Time: " + str(time.time() - m1_start_time))
