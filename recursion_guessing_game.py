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

def rounds(tries, num_of_rounds, ):
	import random
	targetnumber = int(random.randint(1, 100))

	if num_of_rounds == 0:
		print "Oops! No more tries!"

	else:
		Guess = game(targetnumber, tries)
		print "Round", num_of_rounds -1
		rounds(tries, num_of_rounds -1)

def bonus(first_half_guess, target):

	if first_half_guess > target:
		print "It is too high"
		bonus(1/2 * first_half_guess)

	elif first_half_guess == target:
		print "You are awesome!!"

	elif first_half_guess < target:
		print "It is too high"
		bonus((1/2 * first_half_guess) + first_half_guess)

def main():
	tries = 5
	num_of_rounds = 3
	Rounds = rounds(tries, num_of_rounds)

	target = raw_input("Target number: ")
	first_half_guess = 50
main()
