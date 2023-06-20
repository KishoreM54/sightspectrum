def add(num1: int, num2: int) -> int:
	"""Add two numbers"""
	num3 = num1 + num2

	return num3

# Driver code
num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")
##
##-----------------------positional argument--------

def char(monday,friday):
    print(f"{monday} and ends with {friday}!.....")
    
char("1st_day=friday","end_day")

def func(age,time,gender):
    print(f"kishore personal detail is:",int(age),float(time),gender)
func(26,9,"male")

def func(x,y,z):
    a=(x+y)*z
    b=(x-(-z))//5
    print(a,b)
func(2,3,4)

##----------------lambda in functions-
func = lambda x, y, z: (x + y) * z, (x - (-z)) // 5
result = func(2, 3, 4)
print(result[0], result[1])
##----------------to find length of arguments-----
def count_lengths(*parameters):
    lengths= [len(parameter) for parameter in parameters]
    return lengths
print(count_lengths({"dad":"mom"},(440009,9899),"dance"))
#------------------find even or odd---------------
def evenodd(x):
    if x%2 == 0:
        print("its_even")
    else:
        print("its_odd")
evenodd(43)
evenodd(3789456)
##-----------default argument-------
def greet(name, message):
    print(f"{message}, {name}!")
greet("kishore",69)
greet(69,"kishore")
greet(69,message="kishore")
greet(name=69,message="kishore")
greet("kishore","hai")
greet(69,message="find")
greet(55,message="lkj"))

def greet(name, message ,age=54):
    print(f"{message}, {name},{age}!") #.......(keyword arg.....end is always written as default arg)
greet(69,message="donkey",age="fish")

greet(69,"message",age=26)

def greet(name, message):
    print(f"{message}, {name}!")

greet("Alice", "Hello")

def dancer(myself,yourself):
    print(f"{myself} is my name and what about you {yourself}!...")
dancer("kishore","ilakya")
##-------------------*arg-----------
def concatenate_strings(*args):
    result = ""
    for arg in args:
        result += arg
    return result
##
### Calling the function with different numbers of arguments
print(concatenate_strings("Hello", " ", "World"))  # Output: "Hello World"
print(concatenate_strings("Python", " ", "is", " ", "awesome"))  # Output: "Python is awesome"
print(concatenate_strings("I", " ", "love", " ", "Python", " ", "programming"))  # Output: "I love Python programming"

def func(*args):
    result=""
    for arg in args:
        result += arg
    return result
print(func("hello"," " ,"daddy"))



      
    

 


























