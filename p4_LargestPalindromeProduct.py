import time

#Direct Loop
print("Reverse Loop:")

m1_start_time = time.time()

max = 0

def check_palindrome(num):
	reverse = 0
	org = num

	while num > 0:
		reverse = reverse * 10 + num % 10
		num = num // 10

	return reverse == org  

for i in range(999,1,-1):
	for j in range(999, i, -1):
		prod = i * j

		if prod > max: 
			if check_palindrome(prod) == True:
				max = prod
		else:
			break

print("Answer: " + str(max) + "; Time: " + str(time.time() - m1_start_time))

#Add variation with mathematical tweaking