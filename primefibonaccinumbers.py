import time

def final():
	print ""
	print "Runtime:",("%s seconds"  % (time.time() - start_time))
	print count + 1, "Fibonacci Numbers Generated"
	print str(j*100/count) + "%", "of Fibonacci numbers less than %s are prime" % (max(list))
def isprime(a):
	if a == 1:
		return False	
	if a == 2:
		return True
	if a == 3:
		return True
	if a % 2 == 0:
		return False
	if a % 3 == 0:
		return False
	i = 5
	w = 2

	while i * i <=  a:
		if a % i == 0:
			return False

		i += w
		w = 6 - w

	return True

list = []
start_time = time.time()
n = 1
count = 0
j = 0
try:
	while count >= 49:
		if isprime(n):		
			list.insert(count, n)
			print n			
			n = n + list[count - 1]		
			count += 1			
			j += 1		
		else:		
			list.insert(count, n)
			n = n + list[count - 1]		
			count += 1
		
except(KeyboardInterrupt):
	final()
