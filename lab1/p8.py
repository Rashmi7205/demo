num = int(input('Enter number'))
sum=0
while (num!=0):
    sum+=num%10
    num//=10
temp = str(sum)
print(temp[::-1]== temp)    
