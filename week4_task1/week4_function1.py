#-------------------functions----------------------
def add():
    a=int(input("enter var_1:"))
    b=int(input("enter var_2:"))
    print(a+b)
var = add()
##print(var)
if var > 20:
    print("done")
else:
    print("not_done")

def add():
    a=int(input("enter var_1:"))
    b=int(input("enter var_2:"))
    print(a+b)

def add():
    a=int(input("enter var_1:"))
    b=int(input("enter var_2:"))
    print(a+b)
print(add())
##
##------------fuction with argument-----------
def glass(name):
    print("kishore",name)
glass("value")
def flash(number):
    print((1,2,3,4,5),number)
flash("total_number")

def flash(number):
    print((1,2,3,4,5),"can you please thell me the total amount:",number)
flash("total_number")

def dance(name,age,gender):
    print("bio_data",(name,age,gender))
dance("kishore",26,"male")

def dance(name, age ,gender):
    print("bio_data",(name,age,gender))
dance("kishore",26,"male")



def fun(height,weight,size):
    print("kishore_data",int(height),float(weight),int(size))
fun(5,6,33)
 
def dance(name, age ,gender):
    print("bio_data",name,age,gender)
dance("kishore",26,"male")
#------------------------function with default argument-------------
def func(name,fruit={"do","it","again"}):
    print("horse",name,fruit)
func("camel")

##
def func(fruit=["apple"],name=["mango"]):
    print(fruit,name)
func()    
func(fruit="king")
func("kishore","mango")
func(name="ston")

def func(name=None, fruit):
    if name is None:
        name = "mango"
    print(name, fruit)
##
##func("gopi")

def greet(name, message="Hello"):
    print(f"{message}, {name}!")
##
### Calling the function without providing the message argument
##greet("Alice")
### Output: Hello, Alice!
##
### Calling the function and providing both name and message arguments
##greet("Bob", "Hi")
### Output: Hi, Bob!

def great(name,message="sun_set"):
    print(f"{message},{name}!....")
great("on_east")

def great(name,message="sun_set"):
    print(f"{message},{name}!....")
great("on_east","hi")

def func(a,b):
    x=a+b
    y=a-b
    z=(a*b)/a
    print(a,b)
    print(x,y,z)
func(4,5)


def func(name,dance="sun"):
    print(f"{dance},{name}!...")
func("1st_name","last_name")
func("last_name")

def func(name):
    print(name+"darla")
func("agnes")
func("aron")

##----------positional argument-----

##
def greet(name, message):
    print(f"{message}, {name}!")

greet("Alice", "Hello")

##------keyword argument--------------

##
def greet(name, message):
    print(f"{message}, {name}!")

greet("Alice",45)
 Output: Hello, Alice!
---------default argument-----
def greet(name, message="Hello"):
    print(f"{message}, {name}!")

greet("Alice","gayu")

##greet("Bob", "Hi")

def my_func(*sun):
    for arg in sun:
        print(arg)

my_func("apple", "banana", "cherry")

##---------*args--------------
####def my_sons(*kids):
####    print("my younger son is :",kids[2])
####my_sons("ajai","ajith","jai","karthi")
##
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

##Return Values
##To let a function return a value, use the return statement

def my_func(a):
    return a*5
    pass
    
print(my_func(5))
print(my_func(10))
    



















































































    

