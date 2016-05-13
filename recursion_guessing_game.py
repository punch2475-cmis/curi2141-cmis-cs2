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

def bonus(minimum, maximum):
	first_half_guess = 1/2 * maximum

	if first_half_guess == target:
		print "You are awesome!!"
		
	elif first_half_guess > target:
		print "It is too high"
		bonus(minimum, first_half_guess-1)

	elif first_half_guess < target:
		print "It is too low"
		bonus(first_half_guess+1,maximum)

def main():
	tries = 5
	num_of_rounds = 3
	Rounds = rounds(tries, num_of_rounds)

	minimum = 1
	maximum = 100
	target = raw_input("Target number: ")
	Bonus = bonus(minimum, maximum)

main()
