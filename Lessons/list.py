## Lists in python
"""
    Lists are mutable objects supported by python
    List can store any type of variable
    List supports the index mechanism
    List is orderd .
    List is a predefined class in python 
    List preserved the insertion order
    Duplicate elements are  also allowed in list
    +ve and -ve indexing is supported by the list
"""
##------------------------ 
##  DEFINGING A LIST
##------------------------
# l = list()
# print(l,type(l))
# l = []
# print(l,type(l))
l = [1,10.3,"hello"]
# print(l,type(l))
# for i in l: #it can be accsessd using for loop
#     print(i)

##--------------------------------
## input list
##-------------------------------
#List with dynamic input
list = eval(input("Enter list")) #Enter list[10,20,30]
print(list)                     # [10, 20, 30]
print(type(list))               #<class 'list'>

##--------------------------------
##  COMPARISION BETWWEN TWO LISTS
##-------------------------------
# a = [10,20,30]
# b = [10,20,30]
# print(a ==b) #True

# a = [10,20,30]
# b = [30,20,10]
# print(a> b) #false
# print(a<b) #True


##--------------------------------
##  LIST SLICING AND SPLITTING
##-------------------------------
#[start : stop : step]
# l = [1,10,20,20,30,40]
# print(l[::])  #print the list
# print(l[::-1]) #Print the list in reverese
# print(l[1:-1]) #print the list from  1 index to the -1 index
# print(l[2::2]) #[20,30]
# print(l[-1:-5]) #[]
# print(l[-1:-6:-1]) #[40,30,20,20,10]

##--------------------------------
##  OPERATORS SUPPORTED BY LIST
##-------------------------------
# l1 = [10,20,30,40,50]
# l2 = [20,40,60,80]
# print(l1+l2) #[10, 20, 30, 40, 50, 20, 40, 60, 80]
# print(10 in l1) #True
# print(100 in l1) #False
# print(l2*2)  #[20, 40, 60, 80, 20, 40, 60, 80]
# print("Length of the list",len(l1)) #5

##--------------------------------
##  BUILT IN FUNCTIONS SUPPORTED BY LIST
##-------------------------------
l1 = [10,20,30,40,50]
l2 = [20,40,60,80]

# ## Find length of the list
# print(len(l1)) #5
# ## find max element in the list
# print(max(l1)) #50
# ##Find min element of the list
# print(min(l1)) #10
# ##Sort the list
# print(sorted(l1))  #Both returns list object
# print(sorted(l1,reverse=True))
# ##find sum of the list
## print(sum(l1)) #150
print("Index of 10",list.index(10))
list.extend([10,20,30])
print("Extend list ",list)
print("Count occurance",list.count(10))
## print("Remove the element",list.remove(10))
print("Pop element form the list",list.pop())
print(list)
print("Pop Element from aperticular index",list.pop(1))
print(list)

##Ordering Elements of the list
##Reverse the order of the list
list.reverse()
print(list)
##Sort the list
##Sort method only applicable for the homogenous data either it is a error
list.sort()
print(list)
##Sort in reverse order
list.sort(reverse=True)
print(list)

'''
List Comprehension is used for crate a list from a iterable object in a easy
and compact way.
'''

li = [x for x in range(1,10)]
print(li)
s = [x*x for x in range (1,6)]
print(s)
p = [x**2 for x in range(1,5)]
print(p)
# ex:
st = "The quick brown fox jumps over the lazy dog"
s = st.split(' ')
li = [[(word[0].upper()+word[1:]),len(word)] for word in s]
print(li)