MyName = "Curi" #Define MyName variable
MyAgeInYears = 15.4 #Define MyAgeInYears variable
MyHeightInM = 1.59 #Define MyHeightInM variable
lofsquare = 6 #Define lofsquare variable
lofrectangle = 10 #Define lofrectangle variable
hofrectangle = 4 #Define hofrectangle variable
nofmonths = 12 #Define nofmonths variable
AgeInMonths = MyAgeInYears * nofmonths #Define AgeInMonths variable by muntiplying MyAgeInYears variable and nofmonths variable
lifeExpectancy = 80.04 #Define lifeExpectancy variable
LeftToLive = lifeExpectancy - MyAgeInYears #Define LeftToLive variable by subtracting MyAgeInYears variable from lifeExpectancy variable 
MtoFT = 3.2808 #Define MtoFT variable
MyHeightInFeet = MyHeightInM * MtoFT #Define MyHeightInFeet variable by multiplying MyHeightInM with MtoFT variable
AverageFemaleHeight = 1.584960 #Define AverageFemaleHeight variable
DifferenceFromAverage = MyHeightInM - AverageFemaleHeight #Define DifferenceFromAverage by subtracting AverageFemaleHeight variable from MyHeightInM variable
AreaofSquare = lofsquare * lofsquare #Define AreaofSquare by multiplying lofsquare variable with lofsquare variable
VolumeofSquare = lofsquare**3 #Define VolumeofSquare variable by cubing the value of lofsquare variable
HalfofVolume = VolumeofSquare / 2 #Define the HalfofVolume variable by dividing the VolumeofSquare variable by 2
AreaofRectangle = lofrectangle * hofrectangle #Define AreaofRectangle by multiplying the lofrectangle variable with the hofrectangle variable
ninthrectangle = AreaofRectangle * 1.0 #Define ninthrectangle variable by multiplying the AreaofRectangle variable with 1.0
print "Hello!" + "My" "name" + "is"+ MyName #Print out the strings and the value in the variable MyName
print "I" + "am" + str(MyAgeInYears)+ "years"+ "old" #Print out the strings and the value in the variable MyAgeInYears
print "I" + "probably" + "have" + str(LeftToLive) + "years" + "left" + "to" +  "live" #Print out the strings and the value in the variable LeftToLive
print "I"+ "am"+ str(MyHeightInM) + "cm" #Print out the strings and the value in the variable MyHeightInM
print "The"+ "answer" + "to"+ "question"+ str(4) + "is"+ str(AreaofSquare) #Print out the strings and the value in the variable AreaofSquare
print ("The","average", "height","for","girls", "my", "age", "in", "Korea", "is", str(AverageFemaleHeight)) #Print out the strings and the value in the variable AverageFemaleHeight
print ("To", "change", "from", "meter", "to", "feet", ",", "multiply", str(MtoFT)) #Print out the strings and the value in the variable MtoFT
print ("I", "am", str(AgeInMonths), "months","old") #Print out the strings and the value in the variable AgeInMonths
print ("The", "length", "of", "the","square","is", str(lofsquare))#Print out the strings and the value in the variable lofsquare
print ("The","length","of","the","rectange","is",str(lofrectangle))#Print out the strings and the value in the variable lofrectangle
print ";)"*10000 #Print out 10000 winking faces. 
