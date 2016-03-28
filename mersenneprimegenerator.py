import time

start_time = time.time()
def isprime(n):
	if n == 2:
		return True
	if n == 3:
		return True
	if n % 2 == 0:
		return False
	if n % 3 == 0:
		return False

	i = 5
	w = 2

	while i * i <=  n:
		if n % i == 0:
			return False

		i += w
		w = 6 - w

	return True

def final():
	print ""
	print count, "Mersenne primes calculated"
	print "Runtime:",("%s seconds"  % (time.time() - start_time))

count = 0
k = 2
try:
	while k>= 2:
		j = 2**k - 1
		if isprime(j):
			print j
			k = k + 1
			count = count + 1
		else:
			k = k + 1
except(KeyboardInterrupt):
	final()

