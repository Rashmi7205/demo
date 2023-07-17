fname=input('Enter filename which you want to create : ')
f = open(fname,"w")

f.write("Welcome to python\n")
f.write("We learn file Handling\n")
f.write("Python is easy\n")

'''
print("File name = ",f.name)
print("File mode = ",f.mode)
print("File can be readable:",f.readable())
print("Check writeable :",f.writable())
print("Close status",f.closed)
'''
line = ["c Program\n","c++ program\n","java program\n","python program\n"]
f.writelines(line)


f.close()
print("Close status",f.closed)
