import math
def add(x,y):
    return x+y
def sub(a,b):
	return a-b
def mul(d,e):
	return d*e
def div(g,h):
	return g/h
def hours_from_seconds(seconds):
	return seconds/3600
def circle_area(r):
	return r**2*math.pi
def sphere_volume(r):
    return 4.0/3.0 * math.pi*r**3
def avg_volume(a,b):
    volume1=(sphere_volume(a-(1.0/2-a)))
    volume2=(sphere_volume(a-(1.0/2-a)))
    return (volume1+volume2)/2
def area (a,b,c):
    s = (a+b+c) /2
    return (s*(s-a)*(s-b)*(s-c))**0.5
def right_align(word):
    return str((80-len(word))*" " + word)
def center(term):
    return str((40-len(term))*" " + term)
def msg_box(word):
   return "+" + ((len(word)+ 4)*"-") + "+" + "\n" + "|" + (2*" ") + (word) + (2*" ") + "|" + "\n" + "+" + ((len(word)+ 4)*"-") + "+"

x= add(3,4)
y= add(5,6)

a=sub(5,3)
b=sub(8,3)

d=mul(4,4)
e=mul(7,3)

g=div(2,3)
h=div(7,4)

h=hours_from_seconds(86400)
h1=hours_from_seconds(97542)

a1 = circle_area(1)
a2 = circle_area(4)

v1=sphere_volume(5)
v2=sphere_volume(9)

v3=avg_volume(10, 20)
v4=avg_volume(20, 40)

s2=area (1,2,2.5)
s3=area (4,5,5.5)

r = right_align("Hello")
s = right_align("Hey")

f1=center("Hello")
g1=center("hi")

m=msg_box("Hello")
o=msg_box("Hi")
n=msg_box("I eat cats!")
p=msg_box("I eat dogs!")

print msg_box(str(x))
print msg_box(str(y))
print msg_box(str(a))
print msg_box(str(b))
print msg_box(str(d))
print msg_box(str(e))
print msg_box(str(g))
print msg_box(str(h))
print msg_box(str(h))
print msg_box(str(h1))
print msg_box(str(a1))
print msg_box(str(a2))
print msg_box(str(v1))
print msg_box(str(v2))
print msg_box(str(v3))
print msg_box(str(v4))
print msg_box(str(s2))
print msg_box(str(s3))
print msg_box(r)
print msg_box(s)
print msg_box(f1)
print msg_box(g1)
print m
print o
print n
print p
