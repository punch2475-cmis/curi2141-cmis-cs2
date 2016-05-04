def game(guess):
	guess = raw_input("I guess: ")
	if guess == random:
		print "You are AWESOME!"
	elif guess > random:
		print "It is too high"
	elif guess < random:
		print "It is too low"
	else:
		game(guess)

def main():
	import random
	random = random.randint(0, 100)
	Guess = game(0)

main()
