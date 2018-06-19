import time
from math import sqrt, log
from collections import defaultdict

#Lazy Method:
print("Lazy Method - Sieve Of Eratosthenes:")

m1_start_time = time.time()
max_check = 10001

def nth_prime(n):
    
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

    # Save all prime numbers
    for p in range(2, n):
        if prime[p]:
            only_primes.append(p)
    
    return only_primes

limit = int(max_check * log(max_check) + max_check * log(log(max_check))) + 1

primes = nth_prime(limit)

print("Answer: " + str(primes[max_check - 1]) + "; Time: " + str(time.time() - m1_start_time))
