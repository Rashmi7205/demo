list = [3,2,3,-1]
s=0
e=len(list)-1
target = 2
list.sort()
while s<e:
    if list[s]+list[e]==target:
        print(list[s] , " ",list[e])
        s+=1
        e-=1
    elif list[s]+list[e] > target:
        e= e-1
    else:
        s=s+1         

