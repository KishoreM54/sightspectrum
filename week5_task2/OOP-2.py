
##class master:                          #----------creating a class basic one ease to understand
##    def __init__(sun,moon,star):
##        sun.star=moon
##        sun.moon=star
##    def stud1(hari):
##        print("smartest student",hari.star,hari.moon)
##    def stud2(hem):
##        print("lazy boy",hem.star,hem.moon)
##x = master("good","one")
##x.stud1()
##x.stud2()

#--------------encapsulation----------(doubt '__' given even output will came how?)
##class master:
##    def __init__(sun,moon,star):
##        sun.star=moon
##        sun.moon=star
##    def stud1(hari):
##        print("smartest student",hari.star,hari.moon)
##    def stud2(hem):
##        print("lazy boy",hem.star,hem.moon)
##    def func(encap,star):
##        encap.star=star
##x = master("good","one")
##x.stud1()
##x.stud2()
##x.func("bad")
##x.stud2()

#----------------want to print only one parameter in the output--------

##class master:
##    def __init__(sun,moon,star):
##        sun.star=moon
##        sun.moon=star
##    def stud1(hari):
##        print("smartest student",hari.star,hari.moon)
##    def stud2(hem):
##        print("lazy boy",hem.star,hem.moon)
##    def func(var1):
##        print(var1.star)
##x=master("word1","word2")
##x.func()

#------------------new one-------


##class master:
##    def __init__(sun,moon,star):
##        sun.star=moon
##        sun.moon=star
##    def stud1(hari):
##        print("smartest student",hari.star,hari.moon)
##    def stud2(hem):
##        print("lazy boy",hem.star,hem.moon)
##x=master("word1","word2")
##x.stud1()
##print(x.star)
##print(x.moon)



##
##class master:
##    def __init__(sun,moon,star):
##        sun.star=moon
##        sun.moon=star
##    def stud1(hari):
##        print(hari.star,hari.moon)
##    def stud2(hem):
##        print(hem.star,hem.moon)
##x=master("word1","word2")
####x.stud1()
####x.stud2()
##print(x.moon)
##x.moon="night"
##x.stud2()

##
##class tenth:
##    def __init__(var1,var2,var3):
##        var1.var2=var3
##        var1.var3=var2
##      
##    def func(char1):
##        print(char1.var2,char1.var3)
##    def func1(char2,var2):
##        print(char.var2)
##x = tenth("sun","moon")
##print(x.var2)
##x.var2="dark"
##x.func()

##
##class dog:
##    name=""
##    age=0
##dog1=dog()
##dog1.name="tommy"
##dog1.age=10
##
##dog2=dog()
##dog2.name="tiger"
##dog2.age=15
##print(f"{dog1.name} is {dog1.age} years old")
##print(f"{dog2.name} is {dog2.age} years old")
##----encap--------
##
##class master:
##    def __init__(sun,moon,star):
##        sun.__star=moon
##        sun.moon=star
##    def stud1(hari):
##        print(hari.__star,hari.moon)
##    def stud2(hem):
##        print(hem.__star,hem.moon)
##    def func(encap,star):
##        encap.__star=star
##x = master("good","one")
##x.stud1()
##x.stud2()
##x.func("bad")
##x.stud2()

#-----------------polymorphism--------

#---------------1 or 2 or 3 arguments can pass in a single class-------
##class demo():
##    def func(self,a=None,b=None,c=None):
##        if a!=None and b!=None and c!=None:
##            return a+b+c
##        elif a!=None and b!=None:
##            return a+b
##        else:
##            return a
##x=demo()
##print("Result:",x.func(20))

#------------for multiple values------------(method )---------
##
##class demo():
##    def func(self,*args):
##        sum=0
##        for i in args:
##            sum += i
##        print("sum values:",sum)
##x=demo()
##x.func(10,20,30,3.5,4.5,1,1,1,1111,445566,44678,4.56)

##class demo():
##    def func(self,a=None,b=None,c=None):
##        c=a+b+c
##        if a<b:   
##            print("values",c)
##        elif a>c:
##            print("values",a)
##        else:
##            
##            c=a
##        print(c)
##x=demo()
##x.func(5,10,3)
##x.func(10,20)
##x.func(50)

##-------inheritance--------
##class version1:
##    def func1(self):
##        print("blue dhale")
##x=version1()
##x.func1()
##
##class version2(version1):
##    def func1(self):
##        print("blue whale")
##x=version2()
##x.func1()

#single inheritance

##class father:  # 1 base class
##    f_name="mohan"
##    f_age=50
##class son(father): # 1 derive class
##    s_name="kishore"
##    s_age=26
##x=son()
##print("son name is:",x.s_name)
##
#multilevel inheritance
##
##class father:  # 1 base class
##    f_name="mohan"
##    f_age=50
##class mom(father):
##    m_
##class son(father): # 1 derive class
##    s_name="kishore"
##    s_age=26
##x=son()
##print("son name is:",x.s_name)


    







































































        























































        
        
        

























        
