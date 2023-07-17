def fact(num):
    f=1
    while(num!=0):
        f*=num
        num-=1
    return f
num = int(input('Enter number'))
print("factorial of the number =",fact(num))    