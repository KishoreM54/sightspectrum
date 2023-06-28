##-------------------encapsulation-------
class _encap:
    def __init__(name,age,gender):                 #(if a value is only private "x._func()......if both function and value is private "x._encap__func" ")
        name.__age=gender
        name.gender=age
    def __func1(self):
        print(self.__age,self.gender)
    def func2(self):
        print(self.__age,self.gender)
x=_encap("king",26)
x._encap__func1()
x.func2()

##---------print only one argument-------

class encap:
    def __init__(name,age,gender):                
        name.age=gender
        name.gender=age
    def func1(self):
        print(self.age,self.gender)
    def func2(self):
        print(self.age,self.gender)
x=encap(24,"var")
print(x.age)
print(x.gender)
        
##------------change one argument---------

class encap:
    def __init__(name,age,gender):                
        name.gender=gender
        name.age=age

    def func2(self):
        print(self.age,self.gender)
        
    def fun(name,gender):
        name.gender = gender
        
x=encap("var",26)

x.func2()
x.fun("var2")
x.func2()

##--------------polymorphism--------
class encap:
    def __init__(name,age,gender):                
        name.gender=gender
        name.age=age

    def func2(self):
        print(self.age,self.gender)
        
class encap2(encap):
    def func2(self):
        self.age="dark"
        print(self.age,self.gender)
x=encap2("dance","party")
x.func2()

class poly:
    def func(self,a,b,c):
        if a>b or a<c:
            return a+b*c
x=poly()
print(x.func(2,3,4))

class poly:
    def func(self,*args):
        sum=0
        for i in args:
            sum += i
            print(sum)
        print("value :",sum)
x = poly()
x.func(12,455,345)

##----------multiple inheritance------
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)


p1 = Point(2, 5)
p2 = Point(2, 3)

print(p1+p2)

##-------------------data abstraction------------

from abc import ABC, abstractmethod
 
class demo(ABC):
 
    @abstractmethod
    def var(self):
        pass

class demo1(demo):
    def var(self):
        print("i am")

class demo2(demo1):
    def var(self):
        print("i was")

x = demo1()
x.var()

x = demo2()
x.var()


class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Woof!")

class Cat(Animal):
    def sound(self):
        print("Meow!")

class Cow(Animal):
    def sound(self):
        print("Moo!")

dog = Dog()
cat = Cat()
cow = Cow()

dog.sound()  
cat.sound()  
cow.sound() 




























    



        























            
    

























        
