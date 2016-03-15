def guess():
	import random
	minimum = int(raw_input("What is the minimum value? >>>"))
	maximum = int(raw_input("What is the maximum value? >>>"))
	random = random.randint(minimum, maximum)
	print "I am thinking of a number between", minimum, "and", maximum
	guessnumber = str(raw_input("What do you think it is? >>> "))
	difference = abs(guessnumber - random)
	if guessnumber == random:
		return True
	elif guessnumber > random:
		return over False
	elif guessnumber < random:
		return under False

guess()

def correct():
	if guess() == True
		output = """
		The target was {}
		Your guess was {}
		That is correct! You must be a phychic!
		""".format(random, guessnumber)
	elif guess() == over False
		output = """
		The target was {}
		Your guess was {}
		That's over by {}
		""".format(random, guessnumber, difference)
	elif guess() == under False
		output = """
		The target was {}
		Your guess was {}
		That's under by {}
		""".format(random, guessnumber, difference)
correct()

