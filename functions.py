def add(x,y):
    return x+y

z= add(3,4)
print z

def sub(a,b):
	return a-b

c=sub(5,3)
print c

def mul(d,e):
	return d*e

f=mul(4,4)
print f

def div(g,h):
	return g/h
i=div(2,3)

print i

def hours_from_seconds(seconds):
	return seconds/3600
h=hours_from_seconds(86400)
print h

import math
def circle_area(r):
    a = r**2*math.pi
    a1 = area_of_circle(1)

print a1

def sphere_volume(r):
    v = 4.0/3.0 * math.pi*r**3
    v1=volume_of_sphere(5)

print v1

def avg_volume(a,b):
    v=((1.0/6.0*math.pi*a**3)+(1.0/6.0*math.pi*b**3))/2
    v2=avg_volume(10, 20)

print v2
    
def area (a,b,c):
    s = (a+b+c) /2
    s1=(s*(s-a)*(s-b)*(s-c))**0.5
    s2=area (1,2,2.5)
print s2
#from here
def right_align(word):
    return  str ((80-len(word))*" " + word)

print right_align("Hello")
    
def center(term):
    return str ((40-len(term))*" " + term)

print center("Hello")

def msg_box(word):
   return "+" + ((len(word)+ 4)*"-") + "+" + "\n" + "|" + (2*" ") + (word) + (2*" ") + "|" + "\n" + "+" + ((len(word)+ 4)*"-") + "+"

print msg_box("Hello")
print msg_box("I eat cats!")

