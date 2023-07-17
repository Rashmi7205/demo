"""
    ## TUPLES IN PYTHON
    ->These are ordered and immutable objects in python
    ->Tuples and lists are almost same but we can modify the list
    after creation but we can't modify the tuple after the creation
    ->Tuples are created using the (parenthesis) but lists are created by
    {curly braces}
    ->Tuples supports less methods than the list

"""
##----------------
##  DEFINING TUPLE 
##---------------
# t1 = ()
# print("Empty tuple",t1,type(t1))
# t2 = tuple();
# print("Empty tuple",t2,type(t2))
# t3 = (10)
# print(t3,type(t3))
# t4 = 10
# print(t4,"It is not a tuple it is integer",type(t4))
# t5 = 10,20
# print(t5,"Is a tuple",type(t5))
# t = (10,20.4,{10,20,"hello"},"world")
# t = 10,20.4,{10,20,"hello"},"world"
# print("Tuple containing different objects",t)

##-------------------------
##  MODIFYING A TUPLE
##---------------------------
"""
    ** Trying to modify a tuple is error
            t[0] =20
TypeError: 'int' object does not support item assignment

"""
# t= (10)
# t[0] =20

##--------------------------
##  ACSESSING TUPLE ELEMENTS
##--------------------------
# t = (1,20.5,["hello",5,89])
# print(t)
# print(t[0]) #1
# print(t[1.3]) ##TypeError: tuple indices must be integers or slices, not float
# print(t[2][0])  #h3llo
# print(t[-1]) #['hello',5,89]
# print(t[::]) #(1, 20.5, ['hello', 5, 89])
# print(t[::-1]) #(['hello', 5, 89], 20.5, 1)


##--------------------------
##  DELETING TUPLE ELEMENTS
##--------------------------
# t = (1,20.5,["hello",5,89])
# del t[0]  TypeError: 'tuple' object doesn't support item deletion


#Note
tp= (x for x in range(0,8)) //Generator
print(tp)


