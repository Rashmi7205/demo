s1 = {10,20,30}
s2 = {30,40,50,60}
print(type(s1))
s1.add(40)
print(s1)
# s1.pop()
# # print(s1)
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
# s1.difference_update(s2)
# print(s1)
# s1.intersection_update(s2)

print(s1.issubset(s2))
print(s1.issuperset(s2))

print(s1.symmetric_difference(s2))