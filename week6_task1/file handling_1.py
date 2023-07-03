#read a file:

file=open("file1")
x=file.read()
print(x)
file.close()
##
###write a file:
##
file=open("file")
file.write("file content")
file.close()
##
###append a file:

file=open("file","handle")
file.write("\n append new line")
file.close()


#read line by line:

##-------------------------------------------------------------------
##
file=open("file.txt","w")
file.write("trial one")
file.close()

##
##--------------wrile more lines-----
file=open("new file.txt","w")

file_1=["dance\n","party\n","pub\n","club\n"]
file.writelines(file_1)
file.close()
##-------using for loop-----------
file=open("new file.txt","w")
file_1=["dance","party","pub","drink"]
for i in file_1:
    file.write(i+"\n")
file.close()

file=open("new file.txt")
print(file.mode)
print(file.read)
file.close()
##
file=open("new file.txt")
print(file.readable())
print(file.writable())
print(file.read())
print(file.mode)
 
##-------read a file-------
name=open("new file.txt","r")
name_1=name.read()
name.close()
print(name_1)
##_----------for loop to print line by line------

name=open("new file.txt","r")
names=name.readlines()
name.close()
for item in range(3):
    print(names[item])
##--------print the end of the file-------

name=open("new file.txt","r")
names=name.readlines()
name.close()
print(names[-1])

##-------------file is available or not----------
try:
    name=open("new file.txt","r")
    names=name.readlines()
    name.close()
    print(names[3])
    for trial in range(3):
        print(names[trial])
        
except FileNotFoundError:
    print("file not available")
    

class father:
    def func(new file):
        try:
            name=open("new file.txt","r")
            names=name.readlines()
            name.close()
            print(names[3])
    for trial in range(3):
        print(names[trial])
        
        except FileNotFoundError:
            print("file not available")
    x=func(new file)
    print(x)






































