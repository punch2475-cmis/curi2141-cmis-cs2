# My script will give the future life story of an individual in a fairy tale form with the information gathered from the user. The variable "name" contains the name of the user. The "gender" variable contains either M which symbolizes male and F which symbolizing female. "MoneyInPocket" variable contains the information on how much money they have. This variable determines whether the individual is going to be rich or poor in the future. "HowAreYou" variable contains the information on whether they are happy or sad. This variable determines whether you are going to have a happy or a sad life with your family in the future. All these variables are inserted into the story and fills in the blanks. 

def yourstory():
    print """
Once upon a time there was a {} named {}. He/She will {} his/her entire life. He/She will live with a {adj} husband/wife and {} children. The {} has a {} life with your family. You will have {} chance of winning lottery. {interesting facts such as secretly being a prince or being arrested.}
""".format(gender, name) #job using random.random , # random.randit for adj of husband/wife

def information():
	import random
	name=raw_input("What is your name? >>> ")
	gender=raw_input("Are you a male or female? Type M if you are a male and F if you are a female >>> ") 
	MoneyInPocket=raw_input("How much do you have in your pocket in coins? >>> ")
	NumberOfSiblings=raw_input("How many siblings do you have? >>> ")
	HowAreYou=raw_input("Are you happy or sad? >>> ")
	
	#gender
	if gender == "M":
		print "man"

	else:
		print "woman"
	#money
	if MoneyInPocket > len(name):
		print " be rich"

	elif MoneyInPocket == len(name):
		print "be extremely poor"

	elif MoneyInPocket < len(name):
		print "have no money"
	
	#Type of family
	if HowAreYou == "happy":
		print "sad"
	
	else:
		print "happy"

