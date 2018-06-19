import time

#Direct List Comprehension
print("Dynamic Programming:")

m1_start_time = time.time()

limit = 4000000

def even_fibonnaci(limit, num1, num2, sum):
	if num1 > limit:
		return sum

	if num1 % 2 == 0:
		return even_fibonnaci(limit, num1 + num2, num1, sum + num1)
	else:
		return even_fibonnaci(limit, num1 + num2, num1, sum)

print("Answer: " + str(even_fibonnaci(limit, 2, 1, 0)) + "; Time: " + str(time.time() - m1_start_time))

#Sum Formula
print("\nStraightforward Loop:")

fibn1 = 2
fibn2 = 1
sum2 = 0

while(fibn1 < limit):
	if fibn1 % 2 == 0:
		sum2 = sum2 + fibn1
	temp = fibn1
	fibn1 = fibn1 + fibn2
	fibn2 = temp

m2_start_time = time.time()

print("Answer: " + str(sum2) + "; Time: " + str(time.time() - m2_start_time))