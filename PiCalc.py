from __future__ import division
import math
import time

def final():
	#What is output once script is manually terminated
	f = (12*j)**(-1)
	print ""
	print f
	print len(str(f)), "Digits of Pi Calculated"
	print "Runtime:",("%s seconds"  % (time.time() - start_time))
	print n, "steps"

def sigma(k):
	#function that utilizes Chudnovsky algorithm to calculate pi
	return (((-1)**k)*math.factorial(6*k)*(545140134*k + 13591409))/((math.factorial(3*k)*((math.factorial(k))**3)*((640320**3)**(k + .5)))

start_time = time.time()	
j = 0
n = 0
try:
	while n >= 1:
		j += sigma(n)
		n += 1
except(KeyboardInterrupt):
	final()
