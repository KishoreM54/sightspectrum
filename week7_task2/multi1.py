##-------------iniializing----------

import threading
import time
def func(y,x1,name):
    for i in range(y):
        time.sleep(x1)
        print(name,"::thread1")
x=threading.Thread(target=func,args=(5,1,"kish"))
x.start()
x1=threading.Thread(target=func,args=(3,1,"ore"))
x1.start()

import threading
import time
def func(x,y,name):
    for i in range(x):
        time.sleep(y)
        print(name,"=first")
x1=threading.Thread(target=func,args=(3,1,"kish",))
x1.start()
y=threading.Thread(target=func,args=(5,3,"ore",))
y.start()

import threading
import time
def func(x,y,name="son"):
    for i in range(x):
        if x==y:
            print("hy",name)
            #print(i)
        else:
            print("dance",name)
            
    time.sleep(y)
    print(name,"=first")
x1=threading.Thread(target=func,args=(2,2))
x1.start()
x1.join()
y=threading.Thread(target=func,args=(2,1))

y.start()
x1.join()
y.join()



def func():
    print("name")
    print("name1")
    print("name2")
    


def fun():
    print("age")
    print("age1")
    print("age2")
fun()
func()

import threading
x=5
def increment():
    for i in range(5):
        global x
        x += 1
    print("increment:", x)
def decrement():
    for i in range(5):
        global x
        x -= 1
    print("decrement:", x)
    
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=decrement)
thread1.start()
thread1.join()
thread2.start()
thread2.join()


































































