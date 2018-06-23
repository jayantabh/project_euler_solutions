import time
from math import sqrt
from collections import defaultdict

#Direct Loop:
print("Direct Loop:")

m1_start_time = time.time()
max_check = 20161

def GetProperDivisors(n) :
    divisors = [1] 
    for i in range(2, int(sqrt(n) + 1)) :
        if (n % i == 0) :
            if (n / i == i) :
                divisors.append(i)
            else :
                divisors.extend((i, int(n/i)))
    return divisors

def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1
    
    only_primes = set()
    for p in range(2, n):
        if prime[p]:
            only_primes.add(p)

    return only_primes

primes = SieveOfEratosthenes(max_check)

abundant_set = set()
total = 0

for i in range(1, max_check):
	flag = 0
	if i not in primes and i not in abundant_set:
		if sum(GetProperDivisors(i)) > i:
			abundant_set.add(i)

	if i > 46 and i % 2 == 0:
		flag = 1
	else:
		for j in abundant_set:
			if j > i:
				break
			if (i - j) in abundant_set:
				flag = 1
	
	if flag == 0:
		total += i

print("Answer: " + str(total) + "; Time: " + str(time.time() - m1_start_time))

#Using Only Prime Divisors:
print("Using Only Prime Divisors:")

m1_start_time = time.time()

def SieveOfEratosthenes_1(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1
    
    only_primes = []
    for p in range(2, n):
        if prime[p]:
            only_primes.append(p)

    return only_primes

primes = SieveOfEratosthenes_1(max_check)

def SumOfDivisors(n):
	product = 1
	sum_of_divisors = 1
	prime_list = defaultdict(lambda : 0)
	num = n
	i = 0
	while(primes[i] <= num and i < len(primes)):
		if num % primes[i] == 0:
			product *= primes[i]
			num = num // primes[i]
			prime_list[primes[i]] += 1
		else:
			i += 1

	for key in prime_list:
		sum_of_divisors *= ((key ** (prime_list[key] + 1)) - 1)//(key - 1)

	return (sum_of_divisors - n)

abundant_set = set()
total = 0

for i in range(1, max_check):
	flag = 0
	if i not in primes and i not in abundant_set:
		if SumOfDivisors(i) > i:
			abundant_set.add(i)

	if i > 46 and i % 2 == 0:
		flag = 1
	else:
		for j in abundant_set:
			if j > i:
				break
			if (i - j) in abundant_set:
				flag = 1
	
	if flag == 0:
		total += i

print("Answer: " + str(total) + "; Time: " + str(time.time() - m1_start_time))

#Using Only Prime Divisors:
print("Using Only Prime Divisors:")

m1_start_time = time.time()

def SieveOfEratosthenes_1(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1
    
    only_primes = []
    for p in range(2, n):
        if prime[p]:
            only_primes.append(p)

    return only_primes

primes = SieveOfEratosthenes_1(max_check)

def divSum(n) :
    result = 0
   
    for i in range(2,int(sqrt(n))+1) :
        if (n % i == 0) :
            if (i == (n/i)) :
                result = result + i
            else :
                result = result + (i + n//i)

    return (result + 1)

abundant_set = set()
total = 0

for i in range(1, max_check):
	flag = 0
	if i not in primes and i not in abundant_set:
		if divSum(i) > i:
			abundant_set.add(i)

	if i > 46 and i % 2 == 0:
		flag = 1
	else:
		for j in abundant_set:
			if j > i:
				break
			if (i - j) in abundant_set:
				flag = 1
	
	if flag == 0:
		total += i
		
print("Answer: " + str(total) + "; Time: " + str(time.time() - m1_start_time))