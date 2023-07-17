from math import sqrt
a=float(input('Enter side1'))
b=float(input('Enter side2'))
c=float(input('Enter side3'))
if (a+b > c) or (a+c > b) or (b+c > a):
    s=(a+b+c)/2
    area = sqrt(s*(s-a)*(s-b)*(s-c))
    print("{:.1f}".format(area))