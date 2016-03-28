import time
import matplotlib.pyplot as plt

print ""
try:
	n = input("Input whole number:   ")
except (NameError, SyntaxError):
	print "Not a whole number, try again"
	execfile("CollatzWhile.py")
list = []
start_time = time.time()
k = 3
j = len(str(n))
count = 0
while n != 1:
	if n % 2 == 0:
		list.insert(count, n)
		count = count + 1
		n = n / 2
		print n
	elif n % 2 == 1:
		list.insert(count, n)
		count = count + 1
		n = k*n + 1
		print n
else:
	print ""
	print "Input:", list[0]
	print count, "steps"
	print j, "digits"
	print "Runtime:", ("%s seconds" % (time.time() - start_time))
	print "Max value", max(list)
	plt.plot(list)
	plt.ylabel("Partial Sums")
	plt.xlabel("Step")
	plt.show()
	quit()
	#execfile("CollatzWhile.py")
