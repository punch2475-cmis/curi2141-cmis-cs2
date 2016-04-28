def countup(n):
	if n >= 10:
		print "Blastoff!"
	else:
		print n
		countup(n+1)

def main():
	countup(1)
	return

main()

def count_up_from(start, stop):
	if start > stop:
		print "Blastoff!"

	else:
		print start
		count_up_from(start+1, stop)

count_up_from(2,12)


def count_down_from(start, stop):
	if start < stop:
		print "Blastoff!"

	else:
		print start
		count_down_from(start-1, stop)

count_down_from(12,2)

def adder(UserInput, total):

	if UserInput == "":
		return "The sum is " + str(total)	
	else:
		total += float(UserInput)
		UserInput = raw_input("Running total :" + str(total) + "\n" + "Next Number: ")
		return adder(UserInput, total)

def main():
	function = adder(0,0)
	print function


def biggest(number):
	prev_userinput = raw_input("Next Number: ")
	if number == "":
		print number

	elif float(prev_userinput) > number:
		biggest(prev_userinput)

	elif number > float(prev_userinput):
		biggest(number)

def call():
	number = 0
	callingfunction = biggest(number)
call()
