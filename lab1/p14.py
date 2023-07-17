def isPrime(var):
    c=0
    for i in range(1,var+1):
        if var%i == 0:
            c+=1
    return c==2

res_list = []
for i in range(2,257):
    if isPrime(i):
        res_list.append(i)
print(res_list)        
