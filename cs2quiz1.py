#Part 1: Terminology (15 points)
#1 1pt) What is the symbol "=" used for?
#       The "=" symbol is called the assignment operator and its job is to assign a value to a variable
#
#
#2 3pts) Write a technical definition for 'function'
#   A function is a named sequence of statements that performs a computation.
#
#
#3 1pt) What does the keyword "return" do?
#   The return keyword does the job of spitting out the value. 
#
#
#4 5pts) We know 5 basic data types. Write the name for each one and provide two
#   examples of each below
#	1: Integer
#	2: String
#	3: Boolean
#	4: Tuple
#	5: Float
#
#5 2pts) What is the difference between a "function definition" and a 
#        "function call"?
#   Function definition is the process of defining a function, specifies the parameters that are to be inluded in the function and structures the blocks of code. Defining the function makes the function available in the program. 
#    Function call is a command that executes the defined function with the given arguments
#
#
#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them
#	1:Input : In the input part, some value is inserted to the program
#	2:Processing:  In the processing part, the function does the calculation with the give input
#	3:Output : In the output part, the function gives an output or the end result of the processing. 
#
#Part 2: Programming (25 points)
#Write a program that asks the user for the areas of 3 circles.
#It should then calculate the diameter of each and the sum of the diameters 
#of the 3 circles.
#Finally, it should produce output like this:

#Circle  Diameter
#c1      ...
#c2      ...
#c3      ...
#TOTALS  ...

# Hint: Radius is the square root of the area divided by pi

import math
def diameter(x):
    return 2*(math.sqrt(x/math.pi))
def total_diameter(e,f,g):
    return e+f+g

def output(a,b,c,d):
    out="""
c1: {}
c2: {}
c3: {}
Totals: {}
""".format(a,b,c,d)
    return out

def main():
    C1=raw_input("Area of C1: ")
    C2=raw_input("Area of C2: ")
    C3=raw_input("Area of C3: ")
    
    a=diameter(float(C1))
    b=diameter(float(C2))
    c=diameter(float(C3))
    d=total_diameter(a,b,c)
    
    out=output(a,b,c,d)
    print out

main()
