def game(targetnumber, tries):
	guess = int(raw_input("Guess a number from 1 to 100. I guess: "))
	if guess == targetnumber:
		print "You are AWESOME!"

	elif tries == 1:
		print "You are horrible at this game"

	elif guess > targetnumber:
		print "It is too high"
		game(targetnumber, tries-1)

	elif guess < targetnumber:
		print "It is too low"
		game(targetnumber, tries-1)

def rounds(tries, num_of_rounds):
	import random
	targetnumber = int(random.randint(1, 100))

	if num_of_rounds == 0:
		print "Oops! No more tries!"

	else:
		Guess = game(targetnumber, tries)
		print "Round", num_of_rounds -1
		rounds(tries, num_of_rounds -1)

def main():
	tries = 5
	num_of_rounds = 3
	Rounds = rounds(num_of_rounds)

main()
