salary = float(input("Enter salary"))
if salary>30000:
    print(salary+salary*(12/100)+salary*(20/100)-salary*(5/100))
elif salary<=30000 and salary>=15000:
    print(salary+salary*(10/100)+salary*(15/100)-salary*(5/100))
elif salary<=15000 and salary>0:
    print(salary+salary*(7.5/100)+salary*(10/100)-salary*(3.5/100))
else:
    print("invalid salary")

