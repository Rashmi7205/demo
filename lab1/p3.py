sal = float(input('Enter your salry'))
if sal>=20000:
    print("Gross=",500+1000+3000+sal)
    print("Net =",500+1000+3000+sal-sal*.12) 
elif sal>=15000 and sal<20000:
    print("Gross=",300+1000+2000+sal)
    print("Net =",300+1000+2000+sal-sal*.12)  
else:
    print("Gross=",00+000+1500+sal)
    print("Net =",00+00+1500+sal-sal*.12)      

