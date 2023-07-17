##Block of code used to perform a specific task
## Function is Two types in python
##      1.Predefined (language defined)
##      2.userDefined (Defined according to the requirement)
##
## syntax:
## def function_name(parameters):
##      function block
##      return <type>;
## 
# # def : mandatory
## return :optional
# First define the function body then call it.
## 
##      PARAMETERS
##
'''
    Parameters are the inputs to the function.
    If there is any parameter contained by a function,But not
    provided by the function call then we will gwt an error
'''



# def swap(no1,no2):
#     # temp = no2
#     # no2 = no1
#     # no1 = temp
#     no1,no2 = no2,no1
#     print(no1,no2)
#     # list = []
#     # list.append(no1)
#     # list.append(no2)
#     # return list
# swap(10,20)
#define a function
# def main():
#     print("main")
# def python():
#     print("python")
#     java()
# def java():
#     print("java")
# python()    

""" 
    SWAP BETWEEN TWO NUMBERS
def swap(no1,no2):
    # temp = no2
    # no2 = no1
    # no1 = temp
    no1,no2 = no2,no1
    print(no1,no2)
    # list = []
    # list.append(no1)
    # list.append(no2)
    # return list
swap(10,20)
x,y,z = 10,20,30
"""

## Local and Global 
# var = 10
# def main():
#     global var;
#     print("I am main() fun",var)
#     var+=10
#     my_fun()
# def my_fun():
#     global var
#     print("I am my fun",var)

# def ABC():
#     global var
#     var = 10
#     var = var +10
#     print("ABC() :",var)
#     abc()
#     bbsr()
# def abc():
#     global var;
#     var+=10
#     print("abc()",var)
# def bbsr():
#     # var+=10 Error 
#     print("bbsr()",var)    
# ABC()
## Global variable not belongs to any function then that
# #variable is known as global variable
# # It can be accessed by directly in any function ,But not to modify
# #Global key word is used to update any global variable
# # 
# #========LOCAL VARIABLE============
# #If a variable belongs to any function then it is known as the 
# #local variable to that function
# #
# #

##          ARGUMENT CONCEPTS
##====================================================
"""
arguments are two types :
    1)Formal parameter  
        IF it is related to the function defination then it is known as the 
        foraml parameter
    2)Actual parameter
        related to the function calling 

    name of the arguments may or may not be same 

    # Any update in local variable cannot affect the global variable

Example-1
-----------

def ABC():
    global var
    var = 10
    print("ABC() :",var)
    abc()
    bbsr(var) #Actual parameter
def abc():
    global var;
    var=10 +var
    print("abc()",var)
def bbsr(py): # formal parameter
    print("bbsr()",py)     
ABC()

"""

##Types of Arguments
''''
    Therea are 4 types of argument concept in python
    1. positional argument
    2. keyword argument
    3. default argument
    4. variable length argument

    1. POSITIONAL ARGUMENT
    -----------------------
        The positional argument states that the usual parameter of the function
        The value of the arguments are according to the position of the varibale

        ex:
        def sayName(name,age):
            print("i am ",name,"and  i'm",age)
        sayName("Alex",90) #i am  Alex and  i'm 90
        sayName(90, "Alex") #i am  90 and  i'm Alex
     #Here the values of the formal are assigned accordind to their position
     
     2.KEYWORD ARGUMENT
     ------------------
     ->In this the parameters are assigned according to the given keyword
     ->Here the order of argument does not important but the no of argument matters
     Ex:
     def sayName(name,age):
       print("Hello i am",name,"and i am ",age)
    sayName(name="Alex", age=30) # Hello i am Alex and i am  30
    sayName(age=30, name="Alex") # Hello i am Alex and i am  30

    Note:   
        We can use the positional and the keyword argument simontaniously but
        we have to use the positional argument first and after that we can use the 
        key word argument otherwise it will be an error


    3. DEFAULT ARGUMENT
    ----------------------
    ->In this there is a default value for the parameter which is present in the formal paremeter
    ->After one default parameter we can't take non default parameter
    ex:
    def fun(arg ="value" ,arg2 ="value") ===>Valid
    def fun(arg  ,arg2 ="value") ===>Valid
    def fun(arg ="value" ,arg2) ===>InValid

    ex:
    def sayName(name="guest"):
      print("Hello ",name)
    sayName()           #Hello Guest
    sayName("Alex")     #Hello Alex

    4. VARIABLE LENGTH ARGUMENT
    ----------------------------
    Sometime swe pass the number of argument to our function such type of
    arguments are called by variable length argument.

    We can declare a variable length argument by * 
    We can call the function without or with the parameter

    def sum(*n):
        print(n)
        s=0;
        for i in n:
            s+=i
        return s 
    print(sum(1,2,3))  
    
    *n is a tuple
    *kwargs stores the vlaue in dict

'''

## ----------TYPES OF CALLING---------
##-----------------------------------------
"""1    
    

"""
## 
#===============FIRST CLASS OBJECT=========
"""
    // In c ,c++,java we can't define a function within a function
    // but it is possible in python it is known as the first class object
    // Nested function can possible in python but not in c,cpp and java
    //In actual parameter if we pass a function name then that concept 
        is known as first class concept


    def Cpp():
    var = 10
    print("I am super class")
    java()

    def c(): #first class object
        print("i am sub class present in Cpp")
    c()
def java():
    print("I am java pro")
Cpp()       

output-:
I am super class
I am java pro
i am sub class present in Cpp

ex-2
-----
    def main():
    print("main()")
    def newmain():
        print("new main")
    newmain()
    bbsr(newmain)
def bbsr(newmain):
    print("bbsr")
    newmain()
main()  
output:
----------
main()
new main
bbsr
new main
"""

##======================================|
## -------NON-LOCAL KEYWORD-------------|
##======================================|
"""
    Local variable of a function can be accessed in the first class object
    but cannot be modified
    Non local keyword is used to modify the local variable 
"""
##ex-1
# def bbsr(newmain):
#     print("bbsr")
#     newmain()
# def main():
#     var  = 10
#     print("main()",var)
#     def newmain():
#         nonlocal var 
#         var = var + 10
#         print("new main",var)
#     newmain()
#     bbsr(newmain)

# main()    
## output:
## main() 10
## new main 20
## bbsr
## new main 30

##ex-2
#def bbsr(newmain):
#     print("bbsr")
#     newmain()
# def main():
#     var  = 10
#     print("main()",var)
#     def newmain():
#         var1 = 20
#         nonlocal var
#         var = var+10
#         var1 = var1+10
#         print("newmain()",var,var1)
#         def newfun():
#             # var1 = var1+10
#             print("newfun()",var,var1)
#         newfun()    
#     bbsr(newmain)

# main()    
## Differenece between call by value and call by address and call by reference
"""
    python does not support call by value and call by reference concept
    call by reference is two types 
        1)Reference as value type
            number
        2)Reference as reference type 
"""
## Return Statement
"""
    Return is used to terminate a function ,but to terminate a loop break
    is used
    In python return statement retuns multiple value in tuple object

    calling :
        4 types of calling
        --------------------
        ->Position as agrument
        ->keyword as argument
        ->variable length as argument
        ->Default value as argument

        EX
        ----
        def test(regno,name,dept= "arts")
            print("Hello,i am ",name,"my regno is",regno,"& maydeptno",dept)
        
        test(1,"raja","Dsc")
        #test("dsc",1,"rajani")
        test(dept = "cs",regno = 10,name = "raj")
        test(100,dept = "ITM",name = "raj")
        #test(regno = 200,name = "rajani kant","bca") error
        test(regno= 300,name = "rani",dept = "bca")
        test(regno = 300,name= "rani")
        
"""
## Variable length mechanism

# def test(*n):
#     for i in n :
#         print(i,end=" ")
# test()
# test(10,20)
# test(20,30,40)       

##EX of return type
# def test():
#     return 
# x = test()
# print(x,type(x))     #None <class 'NoneType'>

## Ex-2
# def test():
#     return 10,20
# #Boxing mechanism
# x , y = test()
# print(x,y)    10,20
# #using tuple
# x = test()
# print(x)   (10,20)


## LAMBDA FUNCTION
"""
    ->'lambda' keyword is used
    ->Return statement is not allowed
    ->synatx
        name = lambda argument list: exepression/logic 
"""
#ex-
#===
# test = lambda no1,no2:print(no1,no2)
# test(10,20)


##filter Function
# -----------------------------
# Wijtout lambda function
def isEven(x):
    if x%2==0:
        return True
    else:
        return False
l = [x  for x in range(1,11)]
l1 = list(filter(isEven,l))
print(l1)
#With lambda function
l = [x  for x in range(1,11)]
l1 = list(filter(lambda x:x%2==0,l))
print(l1)

## Map Function
'''
    Map function is used to apply some functionality and modification 
    on the given sequence 

    it it generrate a new modified sequences

    syntax:
        ---------
        map(function,sequence)
'''
