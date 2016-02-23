def luckynumber(x,y,v,w):
    return ((y-x)*(v/w))*v+x

def output(name,b):
    out="""
Hello {}
Your lucky number for this month is {}
""".format(name,b)
    return out

def main():
    name=raw_input("Type your name >>>")
    x=raw_input("Type your age >>>")
    y=raw_input("Type the year you were born >>>")
    z=raw_input("Type your favorite number >>>")
    
    a=luckynumber(name,x,y,z)
    
    out=output(name,b)
    print out

main()
