# My script will give them a fairytale of an individual with the information gathered from the user. The variable "name" contains the name of the user. The "gender" variable contains either M which symbolizes male and F which symbolizing female. "MoneyInPocket" variable contains the information on how much money they have. This variable determines whether the individual is going to be rich or poor in the future. "HowAreYou" variable contains the information on whether they are happy or sad. This variable determines whether you are going to have a happy or a sad life with your family in the future. All these variables are inserted into the story and fills in the blanks. 



def SecretOfBirth():
	print "Now lets look at your secrets! Type a,b or c."
	Choice="""
a. I have a dead body in my basement
b. I am a maniac of something that is nasty
c. I am secretly a mermaid
"""
	print Choice
	Answer=raw_input("Type your answer >>> ")
	if Answer == "a":
		return "He/She was secretly a princess in Barbie Dream House who once had a fat, hairy, short but handsome prince by his/her side."
	elif Answer == "b":
		return "He/She was secretly a unicorn and when they were peeing in the bathroom at night, their pee turns into a rainbow and their horn appears. To hide this, he/she had to make sure that she always locked the bathroom door whenever he/she peed."
	elif Answer == "c":
		return "He/She was secretly a psycopath who only kills fish."
        
def information():
	name=raw_input("What is your name? >>> ")
def Gender():
	gender=raw_input("Are you a male or female? Type M if you are a male and F if you are a female >>> ") 
#gender
	if gender == "M":
		return "man"

	else:
		return "woman"

def Money():
	MoneyInPocket=raw_input("How much do you have in your pocket in coins? >>> ")
#money
	if MoneyInPocket > len(name):
		return "rich"

	elif MoneyInPocket == len(name):
		return "extremely poor"

	elif MoneyInPocket < len(name):
		return "had no money"
	
def NumberOfKids():
	NumberOfSiblings=raw_input("How many siblings do you have? >>> ")

def Family():
	HowAreYou=raw_input("Are you happy or sad? >>> ")
#Type of family
	if HowAreYou == "happy":
		return "sad"
	
	else:
		return "happy"

def TypeOfHusbandWife():
	Coins=int(raw_input("How many coins do you have in your pocket? >>> "))
	if Coins > len(name):
		return 1
	RandomRandint=random.randint(Coins, len(name))

#Adj for husband/wife (random.randint)
	if RandomRandint > (len(name)+Coins)/2:
		return "hairy"
    
	elif RandomRandint < (len(name)+Coins)/2:
		return "bald"

	elif RandomRandint == (len(name)+Coins)/2:
		return "unfaithful"
    
	elif RandomRandint > (len(name)+Coins):
		return "sweet"

	elif RandomRandint < (len(name)+Coins):
		return "rich"

def Job():
	RandomRandom=random.random
	guessNumber = lottery()

    #occupation
	if RandomRandom > 0.5:
		return "beggar"

	elif RandomRandom < 0.5:
		return "doctor"

	elif RandomRadom == 0.5:
		return "photographer"

def lottery():
	import random
	answer=random.randint(1,3)
	print "I am thinking of a number between 1 and 3 and it is not a decimal."
	guessnumber = int(raw_input("What do you think it is? >>> "))

    #lottery
	if guessNumber == random:
		return "He/She won the lottery at least 3 times in her life time!"

	elif guessNumber < random:
		return "He/She didn't even have one chance winning the lottery no matter how many times he/she tried because luck was just never on his/her side."

	elif guessNumber > random:
		return "He/She could have won a lottery but didn't try."
  
def yourstory():
    import random
Secret=SecretOfBirth()
State=Money()
Information=information()
Kids=NumberOfKids()
AdjForFamily=Family()
Adjective=TypeOfHusbandWife()
Occupation=Job()
Lottery=lottery()
print """
Once upon a time there was a {} named {}. He/She was {} his/her entire life. He/She lived with a {} husband/wife and {} children. He/She was a {}. {} {} He/She had a {} life with your family.
""".format

yourstory()
