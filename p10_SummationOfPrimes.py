import time
from math import sqrt

#Direct Loop
print("Direct Loop:")

m1_start_time = time.time()
max_check = 2000000

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

print("Answer: " + str(sum(SieveOfEratosthenes(max_check))) + "; Time: " + str(time.time() - m1_start_time))

