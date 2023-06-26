### define a class
##class Bike:
##    name = ""
##    gear = 0
##
### create object of class
##bike1 = Bike()
##
### access attributes and assign new values
##bike1.gear = 11
##bike1.name = "Mountain Bike"
##
##print(f"Name: {bike1.name}, Gears: {bike1.gear} ")
##
##The code you provided defines a class named "Bike." The class has two attributes: "name" and "gear."
##
##To create an object of the class, you initialize an instance called "bike1" by calling the class with empty parentheses: bike1 = Bike(). This creates a new instance of the Bike class and assigns it to the variable "bike1."
##
##You can then access the attributes of the object using dot notation. In this case, you assign a value of 11 to the "gear" attribute of "bike1" (bike1.gear = 11) and the name "Mountain Bike" to the "name" attribute of "bike1" (bike1.name = "Mountain Bike").
##
##Finally, you print the values of the "name" and "gear" attributes using an f-string (print(f"Name: {bike1.name}, Gears: {bike1.gear}")). The f-string allows you to embed the values of the attributes within the string, which will be replaced by their respective values when printed.

### define a class
##class Employee:
##    # define an attribute
##    employee_id = 0
##
### create two objects of the Employee class
##employee1 = Employee()
##employee2 = Employee()
##
### access attributes using employee1
##employee1.employeeID = 1001
##print(f"Employee ID: {employee1.employeeID}")
##
### access attributes using employee2
##employee2.employeeID = 1002
##print(f"Employee ID: {employee2.employeeID}")

##
##class football():
##    pass
##football.name = "kishore"
##football.age = 0



##class MyClass:
##    def __init__(self, name):
##        self.name = name
##
##    def say_hello(self):
##        print("Hello, my name is", self.name)
##
## Creating an instance of MyClass
##obj = MyClass("Alice")
##
## Calling the say_hello() method on the instance
##obj.say_hello()

##class classname:
##    def __init__(self, name, age):
##        self.a = name
##        self.b = age
##
##    def func(self):
##        print(self.a)
##
##a = classname("high", "low")
##a.func()
##
##
##class classname:
##    def __init__(fish,name,age):
##        fish.note = name
##        fish.book = age
##    def func(sel):
##        print("vvv",sel.note,sel.book)
##    def fun(self):
##        print(self.name,self.age)
##a = classname("high","low")
##a.func()
##
##
##class players:
##    def __init__(messi,ronaldo,neymar):
##        messi.fish = ronaldo
##        messi.duck = neymar
##    def func(joy):
##        print("the players are!",joy.fish,joy.duck)
####    def fun(enjoy):
####        print(enjoy.duck,enjoy.fish)
####    def room(players):
####        print("bad boy",players.duck,players.fish)
##    def num(gs):
##        print(gs.fish)
##    
##x= players("good","one")
##x.func()
####x.fun()
####x.room()
##x.num()

##def num(name=1,age=3):
##        print(name,age)
##num("gayu","janu")    
##num()

##class value:
##    def __init__(var1,var2,var3):
##        var1.program = var2
##        var1.access = var3
##    def func_1(swimming):
##        print(swimming.program,swimming.access)
##a = value("feet","foot")
##a.func_1()

##
##class strange:
##    def __init__(name,age,gender):
##        name.age=age
##        name.__gender=gender
##    def fun(dog):
##        print(dog.age,dog.gender)
##x=strange("dance","party")
##x.fun()
##print(x.__gender)
##x.__gender = "male"
##x.fun()             #--------------this function used for changing the external values into the output
##print(x.age)
##x.age="female"
##x.fun()

##
##class strange:
##    def __init__(name,age,gender):
##        name.age=age
##        name.__gender=gender
##    def fun(dog):
##        print(dog.age,dog.__gender)
##    def fun_1(name):
##        print(name.__gender)
##x=strange("dance","party")
##x.fun()
##x.fun_1()
##print(x.age)
##x.age="water"
##                                      #("__" in prefix wherever using is called private value)
##x.fun()



##class strange:
##    def __init__(name,age,gender):
##        name.age=age
##        name.__gender=gender
##    def fun(dog):
##        print(dog.age,dog.__gender)
##    def fun_1(best,gender):
##        best.__gender=gender
##x=strange("dance","party")
##x.fun()
##x.fun_1("dare")
##x.fun()

class doctor:
    def __init__(name,age,time):
        name.age=age
        name.__time=time
    def fun(goat):
        print(goat.age,goat.__time)
    def func(stock,time):#------------this one used for changing private value into output
        stock.__time=time
x=doctor("sign","need")
x.fun()
x.func("story")
x.fun()

        







































































































    





















