no = (int)(input("Enter number To check"))
i = int(1)
c= int()
while i<=no:
    if no%i==0:
        c+=1
    i+=1    
if c==2:
    print("Prime")
else:
    print("Not prime")            