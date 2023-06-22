##----------local variables-------------

def grace():
    message = 'Hello'
    print('Local', message)
grace()
print("message")

#-------------global variables------
age = 23

globals()['age'] = 25
print('The age is:', age)


c = 1

def add(c):
    a = c + 2
    print(c)
add(c)

def outside_function():
    num = 20

    def inside_function():
        global num
        num = 25
    
    print("Before calling inside_function(): ", num)
    inside_function()
    print("After calling inside_function(): ", num)

outside_function()
print("Outside both function: ", num)

##------------------generators in python----

def func():
    n=1
    while n<=10:
        value = n*n
        yield value
        n += 1
a = func()
for i in a:
    print(i)

def demo():
    yield 5
a=demo()
print(a.__next__())
or
print(next(a))


def number():
    a=2
    b=7
    c=a+b
    yield c
    yield a
var=number()
print(next(var))
print(next(var))

def gulab(num):
    sun = num*num
    print(sun)
    return sun
var = gulab(5)
for i in var:
    print("enter total value what we return :",i)

    
























