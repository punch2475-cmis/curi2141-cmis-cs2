
def information():
	print "This program will ask you for 5 integer or float values." + "\n" + "It will calculate the average of all values from 0 inclusive to 10 exclusive." + "\n" + "It will print out whether the resulting average is even or odd."

def wake():
	Introduction = information()
	Number1 = float(raw_input("n0: "))
	if Number1 < 0 or Number1 >= 10:
		print str(Number1) + " is out of range."
		Sum1 = 0
		NofN1 = 0
	else:
		Sum1 = 0+Number1
		NofN1 = 1

	Number2 = float(raw_input("n1: "))
	if Number2 < 0 or Number2 >= 10:
		print str(Number2) + " is out of range."
		Sum2 = Sum1 + 0
		NofN2 = NofN1 + 0 
	else:
		Sum2 = Sum1 + Number2
		NofN2 = NofN1 + 1

	Number3 = float(raw_input("n2: "))
	if Number3 < 0 or Number3 >= 10:
		print str(Number3) + " is out of range."
		Sum3 = Sum2 + 0
		NofN3 = NofN2 + 0
	else:
		Sum3 = Sum2 + Number3
		NofN3 = NofN2 + 1

	Number4 = float(raw_input("n3: "))
	if Number4 < 0 or Number4 >= 10:
		print str(Number4) + " is out of range."
		Sum4 = Sum3 + 0
		NofN4 = NofN3 + 0
	else:
		Sum4 = Sum3 + Number4
		NofN4 = NofN3 +1

	Number5 = float(raw_input("n4: "))
	if Number5 < 0 or Number5 >= 10:
		print str(Number5) + " is out of range."
		Sum5 = Sum4 + 0
		NofN2 = NofN4 + 0
	else:
		Sum5 = Sum4 + Number5
		NofN5 = NofN4 +1

	print Sum5 / NofN5

wake()
