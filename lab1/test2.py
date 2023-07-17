fname = input('Enter file Name')
with open(fname,"w") as f:
    print(f.closed)
print(f.closed)    
