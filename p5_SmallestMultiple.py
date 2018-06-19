import time
from math import sqrt, log
from collections import defaultdict

#Direct Loop
print("Direct Loop:")

m1_start_time = time.time()
product = 1
max_check = 20

def get_prime_factors(num):
	flag = 0
	i = 3
	factors = defaultdict(lambda: 0)

	while num % 2 == 0:
		num = num // 2
		flag = flag + 1

	if flag > 0:
		factors[2] = factors[2] + flag

	while(i * i <= num):
		flag = 0

		while num % i == 0:
			num = num // i
			flag = flag + 1

		if flag > 0:
			factors[i] = factors[i] + flag			

		i = i + 2

	if num > 1:
		factors[num] = factors[num] + 1

	return factors

factors_to_multiply = defaultdict(lambda: 0)

for i in range(2, max_check + 1):
	current_factors = get_prime_factors(i)
	for key in current_factors:
		if factors_to_multiply[key] < current_factors[key]:
			factors_to_multiply[key] = current_factors[key]

for key in factors_to_multiply:
	product = product * (key ** factors_to_multiply[key])

print("Answer: " + str(product) + "; Time: " + str(time.time() - m1_start_time))

#Direct Loop Using Mathematical Corrections:
print("Direct Loop Using Mathematical Optimizations:")

m2_start_time = time.time()
product = 1
max_check = 20
limit = sqrt(max_check)
i = 2
power = 0

def SieveOfEratosthenes(n):
    
    # Create a boolean array "prime[0..n]" and initialize
    #  all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
            
            # Update all multiples of p
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1
    
    only_primes = []
    # Print all prime numbers
    for p in range(2, n):
        if prime[p]:
            only_primes.append(p)

    return only_primes

for i in SieveOfEratosthenes(max_check):
	power = 1
	
	if(i < limit):
		power = int(log(max_check)//log(i))

	product = product * (i ** power)

print("Answer: " + str(product) + "; Time: " + str(time.time() - m2_start_time))
