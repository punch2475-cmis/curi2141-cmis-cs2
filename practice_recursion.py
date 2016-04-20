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

def count_up_from(n, stop):
	if n > stop:
		print "Blastoff!"

	else:
		print n
		count_up_from(n+1, stop)

count_up_from(2,12)
