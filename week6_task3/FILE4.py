
import re

text="The 1dance"
x=re.compile("[0-9]+")
y=x.search(text)
print(y)
##_--------else---------------
##
try:
    file = open("example.txt", "r")
    content = file.read()
    print("File contents:")
    print(content)
except FileNotFoundError:
    print("File not found.")
finally:
    file.close()
    print("File handling complete.")
##-----------------finally-------------
try:
    file = open("example.txt", "r")
except FileNotFoundError:
    print("File not found.")    
else:
    content = file.read()
    print("File contents:")
    print(content)
    file.close()
finally:
    print("jega")      

##
##
try:

   var = 10/2
   print(var1)
except ZeroDivisionError as ex:
    print(ex)
except NameError as j:
    print(j)
else:
    print("else")
    
##except:
##    print("error always")
finally:
  print("finally")
