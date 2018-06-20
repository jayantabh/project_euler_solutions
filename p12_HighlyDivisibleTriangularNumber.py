import time
from math import sqrt, log
from collections import defaultdict

#Get all prime factors and use formula till we find the number:
print("Formula and all prime factors:")

m1_start_time = time.time()
max_check = 500
number_of_divisors = 1
num = 0
i = 1

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

while(number_of_divisors < max_check):
    number_of_divisors = 1
    num = i * (i+1) / 2
    factors_dict = dict(get_prime_factors(num))
    for key in factors_dict:
        number_of_divisors = number_of_divisors * (factors_dict[key] + 1)
    i = i + 1

print("Answer: " + str(num) + "; Time: " + str(time.time() - m1_start_time))

#Direct Loop:
print("Direct Loop:")

m2_start_time = time.time()
max_check = 500
number_of_divisors = 1
num = 0
i = 1

def NumberOfDivisors(n) :
    list = [] 
    count = 0
    for i in range(1, int(sqrt(n) + 1)) :
        if (n % i == 0) :
            if (n / i == i) :
                count = count + 1
            else :
                count = count + 2
    return count

while(number_of_divisors < max_check):
    num = i * (i+1) / 2
    i = i + 1
    number_of_divisors = NumberOfDivisors(num)

print("Answer: " + str(num) + "; Time: " + str(time.time() - m2_start_time))