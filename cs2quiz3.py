#Section 1: Terminology
# 1) What is a recursive function?
#	a recursive function is a computation that recurses or continuously calls itself until it reaches a condition for it to stop.
#
#1/1
#
# 2) What happens if there is no base case defined in a recursive function?
#The base case sets the limit for how many times a function could be called. There will be a runtime error because without the base case the function will not stop and will continue to call itself.
#
#1/1
#
# 3) What is the first thing to consider when designing a recursive function?
#The base case
#
#1/1
#
# 4) How do we put data into a function call?
#By using parameters
#
#1/1
# 
# 5) How do we get data out of a function call?
#By using return
#
#1/1
#
#Section 2: Reading
# Read the following function definitions and function calls.
# Then determine the values of the variables a1-d3.

#a1 = 8
#a2 = 8
#a3 = -1

#b1 = 2
#b2 = 2
#b3 = 4

#c1 = 
#c2 = 4
#c3 = 

#d1 = 6
#d2 = 8
#d3 = 4

#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.


# +2 base case is present (MUST BE LABELED) (0 point)
# +2 recursive case is present (MUST BE LABELED) (2 points)
# +1 base case returns sum/ct (or equivalent) (1 point)
# +2 recursive case filters even numbers (2 points)
# +1 recursive case increments sum and ct correctly (0 point)
# +1 recursive case returns correct recursive call (0 point)
# +1 main function present AND called  (1 point)

def Numbers(user_input, total, odd_numbers):
	user_input = raw_input("Number: ")
	if user_input == "":
		return = float(total)/odd_numbers
		
	elif float(user_input)%2 == 0: 
		total1 = int(user_input) + total
		return Numbers(user_input, total1, odd_numbers+1)
		#Recursive case
	else:
		total2 = total+0
		return Numbers(user_input, total2, odd_numbers)

def Main():
	odd_numbers = 0
	total = 0
	Numbers(user_input, total, odd_numbers)

Main()

