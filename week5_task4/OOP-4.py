##what is encapsulation?
class _myclass:
    def __init__(self):
        self.name="name"
        self.age="age"
        self.__time="time"
    def public(self):
        print("first")
    def _protected(self):
        print("second")
    def __private(self):
        print("third")
    def func(self):
        print("ghj")
x=_myclass()

##x.name
x.public()

##x.age
x._protected()

x._myclass__private()

x.func()

####what is polymorphism?

class animal:
    def sound(self):
        print("animals diff sounds")
class dog(animal):
    def sound(self):
        print("dog barks")
class cat(animal):
    def sound(self):
        print("cat meows")
x=[animal(),dog(),cat()]
for i in x:
    i.sound()

##-----------encap usin multi level func--------
class first:
    def __init__(self,name,age):
        self.name=name
        self.age=26
        age
        
class second:
    def __func1(self):
        print("hi",self.name,self.age)

class third(first,second):
    def func2(self):
        print("hello",self.name,self.age)

x=third("king",26)
x._second__func1()
x.func2()

class father:
    def func(self):
        print("kishore:poor")

class mother(father):
    def func1(self):
        print("kishore:rich")

x=mother()
x.func1()



      
        






































    
    





















