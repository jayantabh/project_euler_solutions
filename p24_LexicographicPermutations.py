import time

#Direct Loop:
print("Direct Loop:")

m1_start_time = time.time()
list_digits = [0,1,2,3,4,5,6,7,8,9]
max_check = 1000000

def GetFactorial(n):
	if n == 1:
		return 1
	else:
		return n * GetFactorial(n-1)

magic_number = ''
sum_of_number_below = 0

i = 9
while(i > 0):
	j = 0
	while(j < len(list_digits)):
		sum_of_number_below += GetFactorial(len(list_digits) - 1)
		if sum_of_number_below >= max_check:
			sum_of_number_below -= GetFactorial(len(list_digits) - 1)
			break
		j += 1
	magic_number += str(list_digits.pop(j))
	i -= 1

magic_number += str(list_digits[0])

print("Answer: " + magic_number + "; Time: " + str(time.time() - m1_start_time))