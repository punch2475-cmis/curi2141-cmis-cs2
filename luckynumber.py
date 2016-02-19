def sub(x,y):
    return y-x

def mul(v,w):
    return v*w


def main():
    name=raw_input(Type your name >>>)
    x=raw_input(Type your age >>>)
    y=raw_input(Type the year you were born >>>)
    z=raw_input(Type your favorite number >>>)

    a=sub(int(x),int(y))
    b=mul(int(a),int(z))
