no1 = (int)(input("Enter first numner"))
no2 = (int)(input("Enter second number"))
temp1 = no1
temp2  = no2
while no1!= no2:
    if no1>no2:
        no1-=no2
    else:
        no2-=no1
print("gcd = ",no1)
print("lcm = ",(temp1*temp2)//no1)            