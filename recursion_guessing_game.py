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
	
def main():
	import random
	targetnumber = int(random.randint(1, 100))
	tries = 5
	Guess = game(targetnumber, tries)
	
main()
