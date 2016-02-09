def Addition(x,y):
    return x+y

z= Addition(3,4)
print z

def Subtraction(a,b):
	return a-b

c=Subtraction(5,3)
print c

def Multipication(d,e):
	return d*e

f=Multipication(4,4)
print f

def Division(g,h):
	return g/h
i=Division(2,3)

print i

def hours_from_seconds(seconds):
	return seconds/3600

print hours_from_seconds(86400)

import math
def area_of_circle(r):
    a = r**2*math.pi
    return a

print area_of_circle(1)

def volume_of_sphere(r):
    v = 4.0/3.0 * math.pi*r**3
    return v

print volume_of_sphere(5)

def avg_volume(a,b):
    v=((1.0/6.0*math.pi*a**3)+(1.0/6.0*math.pi*b**3))/2
    return v

print avg_volume(10, 20)
    
def area (a,b,c):
    s = (a+b+c) /2
    return (s*(s-a)*(s-b)*(s-c))**0.5

print area (1,2,2.5)

def right_align("word")
    w=80-int(len(word)+2),"word"
    
def msg_box()

