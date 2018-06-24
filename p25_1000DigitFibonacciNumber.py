import time

#Direct Loop:
print("Direct Loop:")

m1_start_time = time.time()

f1 = 1
f2 = 2
number_of_digits = 0
i = 1

while(number_of_digits < 1000):
	temp = f1
	f1 = f2
	f2 = f2 + temp

	str_number = str(temp)
	number_of_digits = len(str_number)
	i += 1

print("Answer: " + str(i) + "; Time: " + str(time.time() - m1_start_time))