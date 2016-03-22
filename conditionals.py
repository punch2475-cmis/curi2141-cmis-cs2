# My script will give them life story of an individual with the information gathered from the user. The variable "name" contains the name of the user. The "gender" variable contains either M which symbolizes male and F which symbolizing female. "MoneyInPocket" variable contains the information on how much money they have. This variable determines whether the individual is going to be rich or poor in the future. "HowAreYou" variable contains the information on whether they are happy or sad. This variable determines whether you are going to have a happy or a sad life with your family in the future. All these variables are inserted into the story and fills in the blanks. 

def yourstory():
    print """
Once upon a time there was a {} named {}. He/She was {} his/her entire life. He/She lived with a {adj} husband/wife and {} children. The {} had a {} life with your family. He/She had {} chance of winning lottery. {interesting facts such as secretly being a prince or being arrested.}
""".format(gender, name, MoneyInPocket, ) #job using random.random , # random.randit for adj of husband/wife

def information():
	import random
	name=raw_input("What is your name? >>> ")
	gender=raw_input("Are you a male or female? Type M if you are a male and F if you are a female >>> ") 
	MoneyInPocket=raw_input("How much do you have in your pocket in coins? >>> ")
    Coins=raw_input("How many coins do you have in your pocket? >>> ")
	NumberOfSiblings=raw_input("How many siblings do you have? >>> ")
	HowAreYou=raw_input("Are you happy or sad? >>> ")
	RandomRandint=random.randint(len(name), Coins)
    
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

	#Type of family
	if HowAreYou == "happy":
		print "sad"
	
	else:
		print "happy"

