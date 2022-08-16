from math import sqrt

def triangle_area(a,b,c):
    x =int(a)
    y=int(b)
    z=int(c)
    s = float((x + y + z)/2)
    t = sqrt(s*(s - x)*(s-y)*(s-z))
    return t
