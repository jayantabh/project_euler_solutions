import time

#Direct List Comprehension
print("Direct List Comprehension:")

m1_start_time = time.time()

multiples = [x for x in range(1,1000) if ((x % 3 == 0) or (x % 5 == 0))] 

print("Answer: " + str(sum(multiples)) + "; Time: " + str(time.time() - m1_start_time))

#Sum Formula
print("\nSum Formula:")

m2_start_time = time.time()

def divisible_by(divisor, limit):
	temp_limit = int(limit/divisor)
	return divisor * (temp_limit * (temp_limit + 1) / 2)

print("Answer: " + str(divisible_by(3,999) + divisible_by(5,999) - divisible_by(15,999)) + "; Time: " + str(time.time() - m2_start_time))