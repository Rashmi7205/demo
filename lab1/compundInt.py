p = int(input("Enter the amount"))
r = int(input("Enter the rate of intrest"))
t = int(input("Enter the time"))
while t > 0:
    p = p + p*t*r /100
    print("Your amount is",p,"after ",t,"year")
    t = t-1
print("Your total amount is",p)    
