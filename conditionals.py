# My script will give them a fairytale of an individual with the information gathered from the user. The variable "name" contains the name of the user. The "gender" variable contains either M which symbolizes male and F which symbolizing female. "MoneyInPocket" variable contains the information on how much money they have. This variable determines whether the individual is going to be rich or poor in the future. "HowAreYou" variable contains the information on whether they are happy or sad. This variable determines whether you are going to have a happy or a sad life with your family in the future. All these variables are inserted into the story and fills in the blanks. 

def yourstory():
    import random
    print """
Once upon a time there was a {} named {}. He/She was {} his/her entire life. He/She lived with a {} husband/wife and {} children. He/She had a {} life with your family. He/She had {} chance of winning lottery. {interesting facts such as secretly being a prince or being arrested.}
""".format(gender, name, MoneyInPocket, RandomRandint, RandomRandint, HowAreYou,  ) #job using random.random , # random.randit for adj of husband/wife
def lottery():
    answer=random.randint(1,3)
    print "I am thinking of a number between 1 and 3 and it is not a decimal."
    guessnumber = int(raw_input("What do you think it is? >>> "))

def SecretOfBirth():
    print "Now lets look at your secrets! Type a,b or c."
    Choice="""
a. I have a dead body in my basement
b. I am a maniac of something that is nasty
c. I am secretly a mermaid
"""
    if Choice == "a":
        return ""
    elif Choice == "b":
        

        
def information():
	import random
	name=raw_input("What is your name? >>> ")
	gender=raw_input("Are you a male or female? Type M if you are a male and F if you are a female >>> ") 
	MoneyInPocket=raw_input("How much do you have in your pocket in coins? >>> ")
    Coins=raw_input("How many coins do you have in your pocket? >>> ")
	NumberOfSiblings=raw_input("How many siblings do you have? >>> ")
	HowAreYou=raw_input("Are you happy or sad? >>> ")
	RandomRandint=random.randint(len(name), Coins)
    RandomRandom=random.random
    lottery()
    SecretOfBirth()

	#gender
	if gender == "M":
		print "man"

	else:
		print "woman"
	#money
	if MoneyInPocket > len(name):
		print "rich"

	elif MoneyInPocket == len(name):
		print "extremely poor"

	elif MoneyInPocket < len(name):
		print "had no money"

	#Adj for husband/wife (random.randint)
    if RandomRandint > (len(name)+Coins)/2
        print "hairy"
    
    elif RandomRandint < (len(name)+Coins)/2
        print "bald"

    elif RandomRandint == (len(name)+Coins)/2
        print "unfaithful"
    
    elif RandomRandint > (len(name)-Coins)
        print "sweet"

    elif RandomRandint < (len(name)-Coins)
        print "rich"
    #number of children
    if RandomRandom > 0.5
        print "beggar"

    elif RandomRandom < 0.5
        print "doctor"

    elif RandomRadom == 0.5
        print "photographer"

	#Type of family
	if HowAreYou == "happy":
		print "sad"
	
	else:
		print "happy"
    #lottery
    if guessnumber == random
        print "He/She won the lottery at least 3 times in her life time!"
    elif guess number < random
        print "He/She didn't even have one chance winning the lottery no matter how many times he/she tried because luck was just never on his/her side."
    elif guess number > random
        print "He/She could have won a lottery but didn't try."

    #Discovery
    
