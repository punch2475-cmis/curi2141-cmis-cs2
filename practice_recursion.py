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


def adder():
	print "Running total: 0 "
	UserInput = raw_input("Next number: ")
	
	if UserInput == "":
		print "The sum is {}"
		exit

	else:
		adder()

def main():
	function = adder()

main()
	
