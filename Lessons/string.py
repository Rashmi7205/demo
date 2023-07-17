## String class
"""
    collection of unicode charracter is known as the string
    string canbe represented by sigle qupote(''),double qoute(""),triple quote(""" """)
"""
##----------------------------------------
##   Defining a string
##----------------------------------------
# s = str()
# print(type(s))  #<class 'str'>

# s = "Hello"
# print(s,type(s)) #HEllo<class 'str'>

# # single quote
# s = 'hello'

# #using double quote
# s ="Hello"

# #using triple quote(multiline strings)
# s = """
#     python
#     java
#   """
# print(s)

## ----------------------------
##  String Indexing and slicing
##-----------------------------
# s = "Hello"
# print(s[0]) #H
# print(s[1]) #e
# print(s[::]) #PRint the while string
# print(s[::-1])#revese the string
# print(s[:3]) #print from index 0 to the index 2
# print(s[3:]) #print fro 3 to the end of the string
# print(s[1:4]) #print from index 1 tothe index 3
# print(s[-1:-4])

## ----------------------------
##  String reinitialization
##-----------------------------
"""
    String is immutable object so we can't re initailize the string agian
    if we tried to reinitialize it will show error:
              s[0] = 'H'
        TypeError: 'str' object does not support item assignment
"""
# s ="hello"
# # s[0] = 'H' error
# s = "Hello"
# print(s) #Hello

## ----------------------------
##  String Deletion
##-----------------------------
"""
    Strings are immuatable so the characters of the string cannot be deleted
    but the whole string can be delete 

    It can be implemented by the key word 'del'

    If we tries to delete the char of a string it will show an error:
    ##TypeError: 'str' object doesn't support item deletion
        
# """
# s = "Hello"
# #del s[0]
# del s ## Deletes the whole string

## ---------------------------------
##  Operators supported by the string
##----------------------------------

# s= "Hello"
# s1= "world"
##concat Two string
# print(s1+s) #World Hello

## print it multiple times
# print(s*3) #Hello Hello Hello

## in and not in  operator for searching
# print('H' in s) #TRue
# print('H' not in s) #False

## We can also use comparision operators(<, > , >= ,<=) and equality on stirng
# s1= input("Enter first string")
# s2 = input("Enter second string")
# if s1==s2:
#     print("Both strings are equal")
# elif(s1>s2):
#     print("S1 is larger than the s2")
# elif(s1<s2):
#     print("S2 is lrger than s1")
# else:
#     print("Invalid Input strings")







## ----------------------------
##  String Formatting
##-----------------------------

# s = "Hello,"boy"" error
## Using single quotes
# s = 'hello,"raja"'
# print(s)

##Using Escape \
# s = 'hello,\"jack"'
# print(s)

##Using Escape"\"
# s = "Hello,\"jack\""
# print(s)

##  Using format Method
# print("Hi iam {} and I am{}".format("rashmi",19))

## Using positional Argument
# print("Hi iam {0} and I am {1}".format(19,"rashmi"))
## Note :- position always starts from 0 .

## Keyword  argument
# print("{a}{b}{c}".format(a ="name",b=20,c =20.4))

## ----------------------------
##  METHODS SUPPORTED BY STRING
##-----------------------------
# s = "hello World"
##Capitalize the first charracter of the string
# print(s.capitalize())

##print in the center 
# print(s.center(10))

##Count the the no of occurance of a substring in the string
# print(s.count("ll",0,len(s)))

##Removing spaces from the string




# .Examples'

##Wap to accsess the char in forward and backward direction
# st = "Hello world"
# n = len(st)

# i=0
# while i<n:
#     print(st[i])
#     i+=1
# i = n-1
# while i>=0:
#     print(st[i])
#     i-=1

##changing case of string
# str = "Hello world"
# print(str.lower()) #hello world
# print(str.upper()) #HELLO WORLD
# print(str.capitalize()) #Hello world
# print(str.swapcase()) #hELLO WORLD
# print(str.title())  #Hello World


## and ending with  part of the string
#s.startswith(substring)
#s.endswith(substring)
s = "Learning python is very easy"
print(s.startswith("learning")) #false
print(s.startswith("Learning")) #True

print(s.endswith("learning")) #False
print(s.endswith("easy")) #True


##Check if a character present in the string or not
'''
1 ) isalnum() :Returns True if all the characters are alplah numeric in the string(0-9,a-z,A-Z)
2) isalpha() : Returns True if all the characters are alphabet 
3) isdigit() : Returns True  if all the characters are digit in the string
4) islower() : Returns True if all the character s are in lowercase in the string
5) isupper() :Returs True if all the characters in the string are i  the upper acse
6) istitle() :Returns true if the string is in the title case
7) isspace() : Returns True if the string is a space 
'''

print("Rashmi720".isalnum()) #True 
print("Rashmi".isdigit()) #False
print("123".isdigit())   #True
print("Rashmi".isalpha()) #True
print("Rashmi".istitle()) #True
print("rashmi".islower()) #True
print("RASHMI".isupper()) #True
print(" ".isspace()) #True


## ** String Formating
#Using replacement operator {} and format method we can format the string
#formatting 3 types
#       1)Default
#       2)Positional
#       3)Keyword argument
name = "Alex"
age= 21
sal = 100000
print("{} is{} and getting salary {}".format(name,age,sal)) #deafult
print("{0} is {1} and getting salary {2}".format(name,age,sal)) #positional
print("{x} is {y} and getting salary {z}".format(x=name,y=age,z=sal))


##Number formatting
'''
    d->Decimal integer
    f->Floating values.The default precision is 6
    b->Binary Format
    o->octal format
    x->Hexdecimal format(Lowercase)
    X->Hexadecimal format(Uppercase)
'''
print("The integer number is{}".format(123)) #123
print("The integer number is{:d}".format(123)) #123
print("The integer number is{:5d}".format(123)) #   123
print("The integer number is{:05d}".format(123))#00123

##Float numbers
print("The Float value is {}".format(123.4567)) #123.4567
print("The Float value is {:f}".format(123.4567)) #123.456700
print("The Float value is {:8.3f}".format(123.4567)) #123.457
print("The Float value is {:08.3f}".format(123.4567)) #0123.457
print("The Float value is {:08.3f}".format(123.45)) #0123.450
print("The Float value is {:08.3f}".format(6789012334.45)) #6789012334.450

'''
    Note:
        :8.3f
        Total position should be minimum 8
        After decomal 3 places should be there 
        if total place<8 fill 0 
        The extra digit we can take is only zero
'''

##Other Formats
print("Binary form{:b}".format(15)) #1111
print("Octal form {:0}".format(15)) #15
print("Hexadecimal form {:x}".format(154)) #9a
print("Hexadecimal form{:X}".format(154)) #9A
