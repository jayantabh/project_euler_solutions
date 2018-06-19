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

m2_start_time = time.time()

while(fibn1 < limit):
	if fibn1 % 2 == 0:
		sum2 = sum2 + fibn1
	temp = fibn1
	fibn1 = fibn1 + fibn2
	fibn2 = temp

print("Answer: " + str(sum2) + "; Time: " + str(time.time() - m2_start_time))

#Add all third elements of the fibonacci series
print("\nAdd all third elements:")

fibn1 = 1
fibn2 = 1
fibn3 = 2
sum3 = 0

m3_start_time = time.time()

while(fibn3 < limit):
	sum3 = sum3 + fibn3
	fibn1 = fibn2 + fibn3
	fibn2 = fibn1 + fibn3
	fibn3 = fibn1 + fibn2

print("Answer: " + str(sum3) + "; Time: " + str(time.time() - m3_start_time))

#Using recursive formula for even fibonacci numbers: E(n) = 4 * E(n-1) + E(n-2)
print("\nUsing recursive formula:")

fibn1 = 2
fibn2 = 8
sum4 = 2

m4_start_time = time.time()

while(fibn2 < limit):
	sum4 = sum4 + fibn2
	temp = fibn2
	fibn2 = 4 * fibn2 + fibn1
	fibn1 = temp

print("Answer: " + str(sum4) + "; Time: " + str(time.time() - m4_start_time))