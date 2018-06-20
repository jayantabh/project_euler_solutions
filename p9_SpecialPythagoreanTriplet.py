import time
from math import sqrt

#Direct Loop
print("Direct Loop:")

m1_start_time = time.time()
k = [0 , 0]
product = 1

for i in range(1,999):
	for j in range(i + 1,999):
		k[0] = sqrt(i**2 + j**2)
		k[1] = sqrt(j**2 - i**2)
		for m in k:
			if (i + j + m) == 1000:
				product = i * j * m

print("Answer: " + str(product) + "; Time: " + str(time.time() - m1_start_time))

