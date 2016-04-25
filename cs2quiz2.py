#PART 1: Terminology
#1) Give 3 examples of boolean expressions.
#a) ==
#b) >
#c) <
#  3/3
#2) What does 'return' do?
# It spits out a value
#
#1/1
#
#3) What are 2 ways indentation is important in python code?
#a) The indentation is important because when something is indented, it means that it is in that function.
#b) Another reason indentation is important is because it shows the end of the function
#
#2/2

#PART 2: Reading
#Type the values for 12 of the 16 of the variables below.
#
#problem1_a)	36                  /
#problem1_b)	Square root of 3    /
#problem1_c)	0
#problem1_d)	5                   /
#
#problem2_a)	True
#problem2_b)	False
#problem2_c)	False
#problem2_d)	True
#
#problem3_a)	c	0.3
#problem3_b)	b	0.5
#problem3_c)	a	0.5
#problem3_d)	b	0.5
#
#problem4_a)	7
#problem4_b)	5
#problem4_c)	0.125
#problem4_d)	2.5   /
#12/12 

#PART 3: Programming
#Write a script that asks the user to type in 3 different numbers.
#If the user types 3 different numbers the script should then print out the
#largest of the 3 numbers.
#If they don't, it should print a message telling them they didn't follow 
#the directions.
#Be sure to use the program structure you've learned (main function, processing function, output function)

def ThreeNumbers():
	print "Type in three different numbers (decimals are OK!)"
	Number1=float(raw_input("A: "))
	Number2=float(raw_input("B: "))
	Number3=float(raw_input("C: "))
	if Number1>Number2 and Number1>Number3 and not Number1 == Number2 and not Number1 == Number3 and not Number1 == Number3:
		print "The greatest number was ", Number1
	elif Number1 == Number2:
		print "You didn't follow directions"
	elif Number1 == Number3:
		print "You didn't follow directions"
	elif Number2 == Number3:
		print "You didn't follow directions"

	if Number3>Number1 and Number3>Number2 and not Number3 == Number1 and not Number3 == Number2 and not Number1 == Number3:
		print "The greatest number was ", Number3
	elif Number1 == Number2:
		print "You didn't follow directions"
	elif Number1 == Number3:
		print "You didn't follow directions"
	elif Number2 == Number3:
		print "You didn't follow directions"

	if Number1<Number2 and Number2>Number3 and not Number2 == Number3 and not Number2 == Number1 and not Number1 == Number3:
		print "The greatest number was ", Number2
	elif Number1 == Number2:
		print "You didn't follow directions"
	elif Number1 == Number3:
		print "You didn't follow directions"
	elif Number2 == Number3:
		print "You didn't follow directions"

ThreeNumbers()
	
