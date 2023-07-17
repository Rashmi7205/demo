name=input("Enter Student name")
#name=raw_input("Enter Student name") is not supported by python 3
clg_name=input("Enter clg name")
#python 3 takes by default string type of data
rollno=int(input("Enter roll no"))
print("Student name",name)
print("Student Roll no",rollno)
print("Clg name",clg_name)

# id() is to get the address of the variables 
print("Address of name",id(name))
print("Address of rollno",id(rollno))
print("Adress of clg_name",id(clg_name))

# if two variables have same value then it will
# allocate memory in one location