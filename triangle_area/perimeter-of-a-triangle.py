from math import sqrt

def triangle_area(a,b,c):
    s = float((a + b + c)/2)
    area = sqrt(s*(s - a)*(s-b)*(s-c))
    return area

print(triangle_area(3,6,7))