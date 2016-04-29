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
#Adder
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

#Biggest
def biggest(number):
	current_userinput = raw_input("Next Number: ")
	if current_userinput == "":
		print number

	elif float(current_userinput) > number:
		biggest(float(current_userinput))

	elif number > float(current_userinput):
		biggest(number)

def call():
	number = 0
	callingfunction = biggest(number)
call()
#Smallest
def smallest(number1):
	current_userinput = raw_input("Next Number: ")
	if current_userinput == "":
		print number1

	elif float(current_userinput) > number1:
		smallest(number1)

	elif number1 > float(current_userinput):
		smallest(float(current_userinput))

def call():
	number1 = float("inf")
	calling = smallest(number1)

call()
#power
def pow(x,n):
	
	if int(n) == 0:
		return 1
	elif int(n) == 1:
		return n
	elif int(n) < 0:
		return 1/int(n)
	else:
		print int(x)
		pow(n-1)

def caller():
	Number = raw_input("Base Number: ")
	Exponent = raw_input("Exponent: ")
	pow(Number, Exponent)

caller()
