print("Enter your marks")
math = float(input("Enter your math mark"))
phy = float(input("Enter your physics mark"))
chem = float(input("Enter your chemistry mark"))
total = math+phy + chem
per = (total*100/300)
if per > 60 :
    print(f"You have scored A with {per}%")
elif per < 50 and per >= 40:
    print(f"You have scored  B with {per}%")
elif per < 40 and per >= 33:
    print(f"You have scored C with {per}%")   
else:
    print("You need to appear in the exam again")\

print( f"Congratulation you have got {total}mark")