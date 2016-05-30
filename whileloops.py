def countdown(x):
	while x>0:
		print x
		x = x-1

#countdown(10)

def addup(x):

	while x > 0:
		print x
		return x-1

	while x < 0:
		print x
		return x + 1

def grid(w,l):
	width = "." * w
	while (width):
		print (width + "\n")*l

grid(5,3)
