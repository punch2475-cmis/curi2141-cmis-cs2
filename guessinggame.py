def guess():
	import random
	minimum = int(raw_input("What is the minimum value? >>>"))
	maximum = int(raw_input("What is the maximum value? >>>"))
	random = random.randint(minimum, maximum)
	print "I am thinking of a number between", minimum, "and", maximum
	guessnumber = int(raw_input("What do you think it is? >>> "))
	difference = abs(guessnumber - random)

	if guessnumber == random:
		print """
The target was {}
Your guess was {}
That is correct! You must be a phychic!
""".format(random, guessnumber)
	elif guessnumber > random:
		print """
The target was {}
Your guess was {}
That's over by {}
""".format(random, guessnumber, difference)
	elif guessnumber < random:
		print """
The target was {}
Your guess was {}
That's under by {}
""".format(random, guessnumber, difference)
	
guess()
