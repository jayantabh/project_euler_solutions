import time
from math import sqrt, log
from collections import defaultdict
import datetime

#Using Datetime:
print("Using Datetime:")

m1_start_time = time.time()

d = datetime.datetime(1901, 1, 1)
count = 0

while(d < datetime.datetime(2000,12,31)):
	if d.day == 1 and d.strftime("%A") == 'Sunday':
		count += 1
	d += datetime.timedelta(days = 1)

print("Answer: " + str(count) + "; Time: " + str(time.time() - m1_start_time))