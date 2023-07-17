name=input('Enter name')
roll=int(input('Enter roll no'))
math=float(input('Enter math mark'))
phy=float(input('Enter math physics'))
eng=float(input('Enter math english'))
odia=float(input('Enter math odia'))
che=float(input('Enter math chem'))
print("Name:",name)
print("roll no:",roll)
print("marks are:",math,phy,eng,odia,che)
total=math+phy+eng+odia+che
print("Total mark=",total)
per=(total/500)*100
if per>=60:
    print("1st div")
elif per>=50 and per<60:
    print("2nd div")
elif per>=40 and per<50:
    print(" 3rd div")        
else:
    print("Fail")    
