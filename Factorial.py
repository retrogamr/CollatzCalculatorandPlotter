import time

print ""
try:
	n = input("Input whole number:  ")
except (NameError, SyntaxError):
	print "Not a whole number, try again"
	execfile("Factorial.py")
k = n
start_time = time.time()
j = n
if n == 0:
	j = 1
	print ""
	print j
	print ""
	print k,"!"
	print "Runtime:", ("%s seconds" % (time.time() - start_time))
	execfile("Factorial.py")
elif n < 0:
	print "Not a whole number, try again"
	execfile("Factorial.py")
while n > 1:
	j = j*(n-1)
	n = n - 1
else:
	print ""
	print j
	print ""
	print k,"!"
	print "Runtime:", ("%s seconds" % (time.time() - start_time))
	execfile("Factorial.py")
